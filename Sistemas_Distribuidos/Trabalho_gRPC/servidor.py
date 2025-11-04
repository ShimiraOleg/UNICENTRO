import time
import uuid
import threading
import grpc # type: ignore
import sys
from concurrent import futures
from collections import deque

import gRPC_pb2
import gRPC_pb2_grpc

def carregar_palavras(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]
        if not palavras:
            print(f"[ERRO] Arquivo de palavras '{filepath}' está vazio.")
            sys.exit(1)
        print(f"[Server] {len(palavras)} palavras carregadas de '{filepath}'.")
        return palavras
    except FileNotFoundError:
        print(f"[ERRO] Arquivo de palavras não encontrado: '{filepath}'")
        sys.exit(1)
    except Exception as e:
        print(f"[ERRO] Falha ao ler arquivo de palavras: {e}")
        sys.exit(1)

class GameSession:
    def __init__(self, nome_cliente, palavra):
        self.nome_cliente = nome_cliente
        self.palavra = palavra.lower()
        self.letras_chutadas = set()
        self.chutes_restantes = 9
        self.palavra_escondida = ["_"] * len(self.palavra)
        self.status = gRPC_pb2.StatusJogoReply.JOGANDO

    def get_mask_string(self):
        return " ".join(self.palavra_escondida)

    def FazerPalpite(self, palpite):
        palpite = palpite.lower().strip()

        if self.status != gRPC_pb2.StatusJogoReply.JOGANDO:
            return "O jogo já terminou.", self.status

        if not palpite:
            return "Palpite inválido. Envie uma letra ou palavra.", self.status

        if len(palpite) > 1:
            if palpite == self.palavra:
                self.status = gRPC_pb2.StatusJogoReply.GANHOU
                self.palavra_escondida = list(self.palavra)
                return f"Você VENCEU! Acertou a palavra '{self.palavra}'.", self.status
            else:
                self.status = gRPC_pb2.StatusJogoReply.PERDEU
                self.chutes_restantes = 0
                return f"Você PERDEU! O palpite '{palpite}' está incorreto. A palavra era '{self.palavra}'.", self.status
        letra = palpite

        if not letra.isalpha():
            return "Palpite inválido. Envie uma única letra (ou a palavra completa).", self.status
        if letra in self.letras_chutadas:
            return f"Letra '{letra}' já foi tentada.", self.status
        self.letras_chutadas.add(letra)

        if letra in self.palavra:
            acerto = False
            for i, char in enumerate(self.palavra):
                if char == letra:
                    self.palavra_escondida[i] = letra
                    acerto = True
            if "_" not in self.palavra_escondida:
                self.status = gRPC_pb2.StatusJogoReply.GANHOU
                return f"Você VENCEU! A palavra era '{self.palavra}'.", self.status
            return "Acertou!", self.status
        else:
            self.chutes_restantes -= 1
            if self.chutes_restantes <= 0:
                self.status = gRPC_pb2.StatusJogoReply.PERDEU
                return f"Você PERDEU! A palavra era '{self.palavra}'.", self.status
            return "Errou!", self.status

class ForcaServiceServicer(gRPC_pb2_grpc.ForcaServiceServicer):
    def __init__(self, lista_palavras):
        self.lista_palavras = lista_palavras
        self.palavras_disponiveis = set(self.lista_palavras)
        self.jogos_ativos = {}    
        self.leaderboard = deque(maxlen=5) 
        self.lock = threading.Lock() 

    def IniciarJogo(self, request, context):
        with self.lock:
            if not self.palavras_disponiveis:
                print("[Server] Reciclando lista de palavras.")
                self.palavras_disponiveis = set(self.lista_palavras)
            
            palavra = self.palavras_disponiveis.pop()
            
            cliente_id = str(uuid.uuid4())
            game = GameSession(request.nome_cliente, palavra)
            self.jogos_ativos[cliente_id] = game
            
            print(f"[Server] Jogo criado para {request.nome_cliente} (ID: {cliente_id}). Palavra: {palavra}")

            return gRPC_pb2.IniciarJogoReply(
                cliente_id=cliente_id,
                palavra_escondida=game.get_mask_string(),
                chutes_restantes=game.chutes_restantes
            )

    def FazerPalpite(self, request, context):
        cliente_id = request.cliente_id
        palpite = request.palpite 
        
        print(f"[Server] Palpite recebido de {cliente_id}: '{palpite}'")

        with self.lock:
            game = self.jogos_ativos.get(cliente_id)
            if not game:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("ID do jogo não encontrado. Inicie um novo jogo.")
                return gRPC_pb2.StatusJogoReply()

            messagem, new_estado = game.FazerPalpite(palpite)            
            
            if new_estado != gRPC_pb2.StatusJogoReply.JOGANDO:
                print(f"[Server] Jogo {cliente_id} terminou. Resultado: {new_estado}")
                result = gRPC_pb2.ResultadoJogo(
                    nome_cliente=game.nome_cliente,
                    palavra=game.palavra,
                    isVencedor=(new_estado == gRPC_pb2.StatusJogoReply.GANHOU)
                )
                
                self.leaderboard.append(result)                 
                del self.jogos_ativos[cliente_id]
                self.palavras_disponiveis.add(game.palavra)

            return gRPC_pb2.StatusJogoReply(
                estado=new_estado,
                palavra_escondida=game.get_mask_string(),
                chutes_restantes=game.chutes_restantes,
                letras_chutadas="".join(sorted(game.letras_chutadas)),
                messagem=messagem
            )

    def GetLeaderboard(self, request, context):
        print(f"[Server] GetLeaderboard requisitado.")
        with self.lock:
            return gRPC_pb2.GetLeaderboardReply(leaderboard=list(self.leaderboard))

def server(lista_palavras, host='0.0.0.0', port=50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPC_pb2_grpc.add_ForcaServiceServicer_to_server(
        ForcaServiceServicer(lista_palavras), server
    )
    
    listen_addr = f'{host}:{port}'
    server.add_insecure_port(listen_addr)
    server.start()
    print(f"[Server] Rodando em {listen_addr} ...")
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        print("[Server] Parando servidor...")
        server.stop(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Erro: Forneça o caminho para o arquivo de palavras.")
        print("Uso: python servidor.py <arquivo_palavras.txt> [porta]")
        sys.exit(1)
    
    arquivo_palavras_path = sys.argv[1]
    lista_palavras = carregar_palavras(arquivo_palavras_path)
    
    porta_servidor = 50051
    if len(sys.argv) > 2:
        porta_servidor = int(sys.argv[2])

    
    server(lista_palavras, port=porta_servidor)