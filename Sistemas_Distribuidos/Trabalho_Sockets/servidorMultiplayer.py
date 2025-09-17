import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

def handle_client_session(conn1, conn2, addr1, addr2):
    r1 = conn1.makefile('r')
    r2 = conn2.makefile('r')
    try:
        conn1.sendall(b"Voce eh o Jogador 1. Aguarde o outro jogador...\n")
        conn2.sendall(b"Voce eh o Jogador 2. Aguarde o outro jogador...\n")

        while True:
            conn1.sendall(b"Ambos os jogadores estao conectados! Vamos jogar.\n")
            conn2.sendall(b"Ambos os jogadores estao conectados! Vamos jogar.\n")

            conn1.sendall(b"REQUEST_CHOICE\n")
            line1 = r1.readline().strip()
            if not line1:
                print(f"Jogador 1 ({addr1}) desconectou.")
                break
            
            parts1 = line1.split(',')
            if len(parts1) != 3 or parts1[0] != 'CHOICE':
                conn1.sendall(b"INVALID_CHOICE\n")
                continue
            
            try:
                choice1 = int(parts1[1])
                num1 = int(parts1[2])
            except ValueError:
                conn1.sendall(b"INVALID_CHOICE\n")
                continue

            if choice1 not in (1, 2) or not (0 <= num1 <= 10):
                conn1.sendall(b"INVALID_CHOICE\n")
                continue

            choice2 = 1 if choice1 == 2 else 2
            choice1_str = "impar" if choice1 == 1 else "par"
            choice2_str = "impar" if choice2 == 1 else "par"

            conn2.sendall(f"ASSIGNED_CHOICE,oponente:{choice1_str},sua:{choice2_str}\n".encode())
            conn2.sendall(b"REQUEST_NUMBER\n")
            
            line2 = r2.readline().strip()
            if not line2:
                print(f"Jogador 2 ({addr2}) desconectou.")
                break
            
            parts2 = line2.split(',')
            if len(parts2) != 2 or parts2[0] != 'NUMBER':
                conn2.sendall(b"INVALID_NUMBER\n")
                continue
            
            try:
                num2 = int(parts2[1])
            except ValueError:
                conn2.sendall(b"INVALID_NUMBER\n")
                continue
            
            if not (0 <= num2 <= 10):
                conn2.sendall(b"INVALID_NUMBER\n")
                continue

            # Calculate result
            soma = num1 + num2
            resultado = "par" if soma % 2 == 0 else "impar"

            winner = "Jogador 1" if resultado == choice1_str else "Jogador 2"

            message = (f"RESULT,Jogador1 ({choice1_str}) jogou {num1} | "
                       f"Jogador2 ({choice2_str}) jogou {num2} | "
                       f"Soma = {soma} ({resultado}) | Vencedor: {winner}\n")

            conn1.sendall(message.encode())
            conn2.sendall(message.encode())

            conn1.sendall(b"PLAY_AGAIN\n")
            conn2.sendall(b"PLAY_AGAIN\n")

            ans1 = r1.readline().strip().split(',')
            ans2 = r2.readline().strip().split(',')

            play_again1 = (len(ans1) == 2 and ans1[0] == 'PLAY' and ans1[1].lower() == 's')
            play_again2 = (len(ans2) == 2 and ans2[0] == 'PLAY' and ans2[1].lower() == 's')

            if not (play_again1 and play_again2):
                conn1.sendall(b"SESSION_END\n")
                conn2.sendall(b"SESSION_END\n")
                break

    except Exception as e:
        print(f"Erro na sessao com {addr1} e {addr2}: {e}")
    finally:
        conn1.close()
        conn2.close()
        print(f"Sessao finalizada para {addr1} e {addr2}.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(2)
print(f"Servidor aguardando jogadores em {HOST}:{PORT} ...")

while True:
    conn1, addr1 = server.accept()
    print(f"Conectou Jogador 1: {addr1}")
    conn1.sendall(b"Aguardando um segundo jogador para iniciar partida...\n")

    conn2, addr2 = server.accept()
    print(f"Conectou Jogador 2: {addr2}")
    
    thread = threading.Thread(target=handle_client_session, args=(conn1, conn2, addr1, addr2), daemon=True)
    thread.start()