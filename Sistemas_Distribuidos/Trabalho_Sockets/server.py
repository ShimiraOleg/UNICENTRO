import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

def handle_session(conn1, conn2, addr1, addr2):
    r1 = conn1.makefile('r')
    r2 = conn2.makefile('r')
    try:
        conn1.sendall("Você é o Jogador 1. Aguarde o outro jogador...\n".encode())
        conn2.sendall("Você é o Jogador 2. Aguarde o outro jogador...\n".encode())

        while True:
            conn1.sendall("Ambos os jogadores estão conectados! Vamos jogar.\n".encode())
            conn2.sendall("Ambos os jogadores estão conectados! Vamos jogar.\n".encode())

            conn1.sendall("REQUEST_CHOICE\n".encode())
            line = r1.readline()
            if not line:
                print("Jogador 1 desconectou.")
                break
            line = line.strip()
            parts = line.split(',')
            if len(parts) != 3 or parts[0] != 'CHOICE':
                conn1.sendall("INVALID_CHOICE\n".encode())
                continue
            try:
                choice1 = int(parts[1])
                num1 = int(parts[2])
            except ValueError:
                conn1.sendall("INVALID_CHOICE\n".encode())
                continue

            if choice1 not in (1,2) or not (0 <= num1 <= 10):
                conn1.sendall("INVALID_CHOICE\n".encode())
                continue

            choice2 = 1 if choice1 == 2 else 2
            choice1_str = "ímpar" if choice1 == 1 else "par"
            choice2_str = "ímpar" if choice2 == 1 else "par"

            conn2.sendall(f"ASSIGNED_CHOICE,oponente:{choice1_str},sua:{choice2_str}\n".encode())
            conn2.sendall("REQUEST_NUMBER\n".encode())
            
            line2 = r2.readline()
            if not line2:
                print("Jogador 2 desconectou.")
                break
            line2 = line2.strip()
            parts2 = line2.split(',')
            if len(parts2) != 2 or parts2[0] != 'NUMBER':
                conn2.sendall("INVALID_NUMBER\n".encode())
                continue
            try:
                num2 = int(parts2[1])
            except ValueError:
                conn2.sendall("INVALID_NUMBER\n".encode())
                continue
            if not (0 <= num2 <= 10):
                conn2.sendall("INVALID_NUMBER\n".encode())
                continue

            soma = num1 + num2
            resultado = "par" if soma % 2 == 0 else "ímpar"

            vencedor = None
            if resultado == choice1_str:
                vencedor = "Jogador 1"
            else:
                vencedor = "Jogador 2"

            mensagem = (f"RESULTADO,Jogador1({choice1_str}) jogou {num1} | "
                        f"Jogador2({choice2_str}) jogou {num2} | "
                        f"Soma = {soma} ({resultado}) | Vencedor: {vencedor}\n")

            conn1.sendall(mensagem.encode())
            conn2.sendall(mensagem.encode())

            conn1.sendall("PLAY_AGAIN\n".encode())
            conn2.sendall("PLAY_AGAIN\n".encode())

            ans1 = r1.readline()
            ans2 = r2.readline()
            if not ans1 or not ans2:
                break
            ans1 = ans1.strip().split(',')
            ans2 = ans2.strip().split(',')
            ok1 = (len(ans1) == 2 and ans1[0] == 'PLAY' and ans1[1].lower() == 's')
            ok2 = (len(ans2) == 2 and ans2[0] == 'PLAY' and ans2[1].lower() == 's')

            if not (ok1 and ok2):
                conn1.sendall("SESSION_END\n".encode())
                conn2.sendall("SESSION_END\n".encode())
                break

    except Exception as e:
        print("Erro na sessão:", e)
    finally:
        try:
            r1.close()
        except: pass
        try:
            r2.close()
        except: pass
        conn1.close()
        conn2.close()
        print("Sessão finalizada.")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor aguardando jogadores em {HOST}:{PORT} ...")

    while True:
        conn1, addr1 = server.accept()
        print("Conectou:", addr1)
        conn1.sendall("Aguardando um segundo jogador para iniciar partida...\n".encode())

        conn2, addr2 = server.accept()
        print("Conectou:", addr2)
        t = threading.Thread(target=handle_session, args=(conn1, conn2, addr1, addr2), daemon=True)
        t.start()

if __name__ == "__main__":
    main()