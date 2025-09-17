import socket
import random

HOST = '0.0.0.0'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Servidor escutando em {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conectado por {addr}")

    data = conn.recv(1024).decode("utf-8")
    escolha, numero_cliente = data.split(",")
    numero_cliente = int(numero_cliente)
    numero_servidor = random.randint(0, 10)

    soma = numero_cliente + numero_servidor
    resultado = "par" if soma % 2 == 0 else "ímpar"

    if resultado == escolha:
        vencedor = "Cliente"
    else:
        vencedor = "Servidor"

    resposta = (f"Você escolheu {escolha} e jogou {numero_cliente}. "
                f"O servidor jogou {numero_servidor}. "
                f"Soma = {soma} ({resultado}).\n"
                f"Vencedor: {vencedor}!")

    conn.sendall(resposta.encode("utf-8"))
    conn.close()