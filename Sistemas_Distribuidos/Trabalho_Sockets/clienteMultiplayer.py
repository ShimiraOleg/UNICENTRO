import socket
import sys

HOST = '127.0.0.1'
PORT = 5000

def get_player_choice_and_number():
    while True:
        try:
            choice = int(input("Digite 1 para IMPAR ou 2 para PAR: "))
            if choice in (1, 2):
                break
            else:
                print("Digite apenas 1 ou 2.")
        except ValueError:
            print("Entrada invalida. Digite apenas 1 ou 2.")

    while True:
        try:
            number = int(input("Digite um numero de 0 a 10: "))
            if 0 <= number <= 10:
                break
            else:
                print("Numero fora do intervalo (0-10).")
        except ValueError:
            print("Entrada invalida. Digite apenas numeros.")
    return choice, number

def get_player_number():
    while True:
        try:
            number = int(input("Digite um número de 0 a 10: "))
            if 0 <= number <= 10:
                break
            else:
                print("Numero fora do intervalo (0-10).")
        except ValueError:
            print("Entrada invalida. Digite apenas numeros.")
    return number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")

    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            print("Servidor desconectou.")
            break

        for line in data.splitlines():
            line = line.strip()
            if not line:
                continue

            if line == "REQUEST_CHOICE":
                choice, number = get_player_choice_and_number()
                s.sendall(f"CHOICE,{choice},{number}\n".encode())
            elif line.startswith("ASSIGNED_CHOICE,"):
                print(line.replace("ASSIGNED_CHOICE,", "").replace(",", " | "))
            elif line == "REQUEST_NUMBER":
                number = get_player_number()
                s.sendall(f"NUMBER,{number}\n".encode())
            elif line.startswith("RESULT,"):
                print(line.replace("RESULT,", ""))
            elif line == "PLAY_AGAIN":
                while True:
                    ans = input("Jogar novamente? (s/n): ").strip().lower()
                    if ans in ("s", "n"):
                        break
                    else:
                        print("Por favor, digite 's' para sim ou 'n' para não.")
                s.sendall(f"PLAY,{ans}\n".encode())
                if ans == "n":
                    print("Saindo do jogo.")
                    sys.exit(0)
            elif line == "SESSION_END":
                print("Sessão encerrada pelo servidor.")
                sys.exit(0)
            else:
                print(line)


