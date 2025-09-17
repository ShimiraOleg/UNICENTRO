import socket

HOST = '127.0.0.1'
PORT = 5000

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        escolha = int(input("\nDigite 1 para IMPAR ou 2 para PAR: "))
        if escolha == 1 or escolha == 2:
            break
        print("Opcao inválida! Tente novamente.")
    escolha = "impar" if escolha == "1" else "par"
    
    while True:
        numero = int(input("Digite um numero de 0 a 10: "))
        if numero >= 0 and numero <= 10:
            break
        print("Opcao inválida! Tente novamente.")

    mensagem = f"{escolha},{numero}"
    client_socket.sendall(mensagem.encode("utf-8"))
    data = client_socket.recv(1024)
    print("\nResultado:", data.decode("utf-8"))
    client_socket.close()

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != "s":
        print("Saindo do jogo!")
        break
