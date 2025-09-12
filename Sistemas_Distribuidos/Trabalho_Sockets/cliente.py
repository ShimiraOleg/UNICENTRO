#!/usr/bin/env python3
import socket
import sys

HOST = '127.0.0.1'   # troque para o IP do servidor se estiver em máquinas diferentes
PORT = 5000

# Para limpar o buffer de entrada (POP!/Ubuntu/Unix)
try:
    import termios
    has_termios = True
except Exception:
    has_termios = False

def flush_stdin():
    if has_termios:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def input_choice_and_number():
    while True:
        try:
            flush_stdin()
            escolha_num = int(input("Digite 1 para ÍMPAR ou 2 para PAR: "))
            if escolha_num in (1,2):
                break
            else:
                print("Digite apenas 1 ou 2.")
        except ValueError:
            print("Digite apenas 1 ou 2.")
    while True:
        try:
            flush_stdin()
            numero = int(input("Digite um número de 0 a 10: "))
            if 0 <= numero <= 10:
                break
            else:
                print("Número fora do intervalo.")
        except ValueError:
            print("Digite apenas números.")
    return escolha_num, numero

def input_only_number():
    while True:
        try:
            flush_stdin()
            numero = int(input("Digite um número de 0 a 10: "))
            if 0 <= numero <= 10:
                break
            else:
                print("Número fora do intervalo.")
        except ValueError:
            print("Digite apenas números.")
    return numero

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    try:
        while True:
            data = s.recv(4096)
            if not data:
                print("Servidor desconectou.")
                break
            for line in data.decode().splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("Você é") or line.startswith("Ambos"):
                    print(line)
                elif line == "REQUEST_CHOICE":
                    escolha_num, numero = input_choice_and_number()
                    s.sendall(f"CHOICE,{escolha_num},{numero}\n".encode())
                elif line.startswith("ASSIGNED_CHOICE"):
                    print(line.replace(',', ' | '))
                elif line == "REQUEST_NUMBER":
                    numero = input_only_number()
                    s.sendall(f"NUMBER,{numero}\n".encode())
                elif line.startswith("RESULTADO,") or line.startswith("RESULT,") or line.startswith("RESULTADO") :
                    print(line.replace("RESULTADO,", "").replace("RESULT,",""))
                elif line == "PLAY_AGAIN":
                    while True:
                        ans = input("Jogar novamente? (s/n): ").strip().lower()
                        if ans in ('s','n'):
                            break
                    s.sendall(f"PLAY,{ans}\n".encode())
                    if ans == 'n':
                        print("Saindo do jogo.")
                        return
                elif line == "SESSION_END":
                    print("Sessão encerrada pelo servidor.")
                    return
                elif line == "INVALID_CHOICE" or line == "INVALID_NUMBER":
                    print("Entrada inválida segundo o servidor. Tente de novo.")
                else:
                    print(line)
    finally:
        s.close()

if __name__ == "__main__":
    main()

