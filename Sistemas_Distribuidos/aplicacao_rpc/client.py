import grpc
import blackjack_pb2
import blackjack_pb2_grpc

def print_hand(hand):
    return ", ".join([f"{c.value} de {c.suit}" for c in hand.cards])

def run():
    nome = input("Digite seu nome: ")

    # Conecta ao servidor (use o IP da máquina do servidor se estiver em rede)
    channel = grpc.insecure_channel('10.214.189.215:50051')
    stub = blackjack_pb2_grpc.BlackjackStub(channel)

    # Inicia o jogo
    response = stub.StartGame(blackjack_pb2.GameRequest(player_name=nome))
    print(f"\n{response.message}")
    print(f"Sua mão: {print_hand(response.player_hand)} (Pontuação: {response.player_score})")
    print(f"Mão do Dealer: {print_hand(response.dealer_hand)} (Pontuação: {response.dealer_score})")

    # Loop de jogadas
    while not response.game_over:
        acao = input("\nDigite [h] para puxar carta (hit) ou [s] para parar (stand): ").strip().lower()

        if acao == 'h':
            response = stub.Hit(blackjack_pb2.GameRequest(player_name=nome))
        elif acao == 's':
            response = stub.Stand(blackjack_pb2.GameRequest(player_name=nome))
        else:
            print("Opção inválida.")
            continue

        print(f"\n{response.message}")
        print(f"Sua mão: {print_hand(response.player_hand)} (Pontuação: {response.player_score})")
        print(f"Mão do Dealer: {print_hand(response.dealer_hand)} (Pontuação: {response.dealer_score})")

        if response.game_over:
            print("\nJogo finalizado!\n")
            break

if __name__ == '__main__':
    run()
