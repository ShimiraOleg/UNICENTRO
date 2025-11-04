import grpc # type: ignore
import sys
import gRPC_pb2
import gRPC_pb2_grpc

def print_status(res):
    """Helper para imprimir o estado do jogo."""
    print(f"\n>> {res.messagem} <<")
    print(f"Palavra:  {res.palavra_escondida}")
    print(f"Letras Chutadas: {res.letras_chutadas}")
    print(f"Chances:  {res.chutes_restantes}")

def run(endereco_server='localhost:50051', nome='Jogador'):
    print(f"[Cliente] Conectando ao servidor em {endereco_server} como '{nome}'...")
    try:
        with grpc.insecure_channel(endereco_server) as channel:
            stub = gRPC_pb2_grpc.ForcaServiceStub(channel)
            start_req = gRPC_pb2.IniciarJogoRequest(nome_cliente=nome)
            start_res = stub.IniciarJogo(start_req)
            cliente_id = start_res.cliente_id

            print("[Cliente] Pedindo para iniciar um novo jogo...")
            print(f"[Cliente] Jogo iniciado! ID da sessão: {cliente_id}")
            print(f"Palavra:  {start_res.palavra_escondida}")
            print(f"Chances:  {start_res.chutes_restantes}")

            while True:
                palpite = ""
                while not palpite:
                    palpite = input("\nDigite seu palpite (uma letra ou a palavra inteira): ").strip().lower()

                palpite_req = gRPC_pb2.PalpiteRequest(cliente_id=cliente_id, palpite=palpite)
                status_res = stub.FazerPalpite(palpite_req)

                print_status(status_res)
                if status_res.estado != gRPC_pb2.StatusJogoReply.JOGANDO:
                    print("\n" + "="*30)
                    print("         FIM DE JOGO!")
                    print("="*30)                    
                    try:
                        leaderboard_req = gRPC_pb2.GetLeaderboardRequest()
                        leaderboard_res = stub.GetLeaderboard(leaderboard_req)
                        print("Painel de Jogadores:")
                        if not leaderboard_res.leaderboard:
                            print(" (Painel vazio)")
                        else:
                            for i, resultado in enumerate(leaderboard_res.leaderboard):
                                status_str = "GANHOU" if resultado.isVencedor else "PERDEU"
                                print(f" {i+1}. {resultado.nome_cliente} - {status_str} (Palavra: {resultado.palavra})")
                    
                    except grpc.RpcError as e:
                        print(f"[ERRO RPC] Falha ao buscar placar: {e.details()}")
                    break 
    except grpc.RpcError as e:
        print(f"\n[ERRO RPC] Falha ao conectar ou comunicar com o servidor:")
        print(f"  Status: {e.code()}")
        print(f"  Detalhes: {e.details()}")
    except KeyboardInterrupt:
        print("\n[Cliente] Jogo interrompido pelo usuário.")

if __name__ == '__main__':
    server_addr = sys.argv[1] if len(sys.argv) > 1 else 'localhost:50051'
    nome = sys.argv[2] if len(sys.argv) > 2 else 'Cliente'
    run(server_addr, nome)