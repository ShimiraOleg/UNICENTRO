import grpc
from concurrent import futures
import random
import blackjack_pb2
import blackjack_pb2_grpc

# --- Funções Auxiliares ---

def create_shuffled_deck():
    """Cria e retorna um baralho de cartas embaralhado."""
    suits = ["Copas", "Ouros", "Paus", "Espadas"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(blackjack_pb2.Card(suit=suit, value=value))
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    """Calcula a pontuação de uma mão de cartas, ajustando os Ases."""
    score = 0
    aces = 0
    for card in hand.cards:
        if card.value in ["J", "Q", "K"]:
            score += 10
        elif card.value == "A":
            aces += 1
            score += 11
        else:
            # Garante que o valor é um número antes de somar
            try:
                score += int(card.value)
            except ValueError:
                # Caso haja algum valor inválido, embora improvável com o baralho criado
                pass

    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# --- Implementação do Serviço gRPC ---

class BlackjackServicer(blackjack_pb2_grpc.BlackjackServicer):
    def __init__(self):
        # player_name -> {"player_hand": Hand, "dealer_hand": Hand, "deck": [Card]}
        self.games = {}

    def _get_card_from_deck(self, player_name):
        """Puxa uma carta do baralho do jogo do jogador e a retorna."""
        game_data = self.games.get(player_name)
        if game_data and game_data["deck"]:
            return game_data["deck"].pop(0) # Remove e retorna a primeira carta
        return None

    def StartGame(self, request, context):
        player_name = request.player_name

        # Novo Baralho Embaralhado para este jogo
        deck = create_shuffled_deck()

        # Distribui 2 cartas para o jogador e 2 para o dealer
        player_hand = blackjack_pb2.Hand(cards=[deck.pop(0), deck.pop(0)])
        dealer_hand = blackjack_pb2.Hand(cards=[deck.pop(0), deck.pop(0)])

        # Armazena o estado do jogo, incluindo o baralho restante
        self.games[player_name] = {
            "player_hand": player_hand,
            "dealer_hand": dealer_hand,
            "deck": deck
        }

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        return blackjack_pb2.GameResponse(
            message=f"Jogo iniciado para {player_name}!",
            player_hand=player_hand,
            dealer_hand=dealer_hand,
            player_score=player_score,
            dealer_score=dealer_score,
            game_over=False
        )

    def Hit(self, request, context):
        player_name = request.player_name
        game = self.games.get(player_name)

        if not game:
            return blackjack_pb2.GameResponse(message="Jogo não iniciado.", game_over=True)

        # Puxa uma carta nova do baralho específico do jogo
        card = self._get_card_from_deck(player_name)
        
        if card is None:
             return blackjack_pb2.GameResponse(message="Baralho vazio. Fim do jogo.", game_over=True)

        game["player_hand"].cards.append(card)

        player_score = calculate_score(game["player_hand"])
        dealer_score = calculate_score(game["dealer_hand"])

        msg = f"{player_name} puxou {card.value} de {card.suit}."

        game_over = False
        if player_score > 21:
            msg += " Você estourou! Dealer vence."
            game_over = True

        return blackjack_pb2.GameResponse(
            message=msg,
            player_hand=game["player_hand"],
            dealer_hand=game["dealer_hand"],
            player_score=player_score,
            dealer_score=dealer_score,
            game_over=game_over
        )

    def Stand(self, request, context):
        player_name = request.player_name
        game = self.games.get(player_name)

        if not game:
            return blackjack_pb2.GameResponse(message="Jogo não iniciado.", game_over=True)

        player_hand = game["player_hand"]
        dealer_hand = game["dealer_hand"]

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        # Dealer joga até 17 ou mais, puxando do mesmo baralho
        while dealer_score < 17:
            card = self._get_card_from_deck(player_name)
            if card is None:
                 break # Não há mais cartas no baralho
            dealer_hand.cards.append(card)
            dealer_score = calculate_score(dealer_hand)

        # Determinar resultado
        if dealer_score > 21 or player_score > dealer_score:
            msg = f"Você venceu! Dealer fez {dealer_score}."
        elif dealer_score == player_score:
            msg = f"Empate! Dealer também fez {dealer_score}."
        else:
            msg = f"Dealer venceu com {dealer_score}."

        return blackjack_pb2.GameResponse(
            message=msg,
            player_hand=player_hand,
            dealer_hand=dealer_hand,
            player_score=player_score,
            dealer_score=dealer_score,
            game_over=True
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    blackjack_pb2_grpc.add_BlackjackServicer_to_server(BlackjackServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()