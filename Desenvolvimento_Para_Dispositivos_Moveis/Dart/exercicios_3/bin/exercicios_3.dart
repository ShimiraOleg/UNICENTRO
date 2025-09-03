enum Naipe { 
  COPAS, OUROS, ESPADA, PAUS
}
enum Valor { 
  AS, DOIS, TRES, QUATRO, CINCO, SEIS, SETE, OITO, NOVE, DEZ, VALETE, DAMA, REI
}

void main(List<String> arguments) {
  Baralho baralhoPoker = Baralho();
  baralhoPoker.embaralhar();
  Card carta1 = baralhoPoker.comprar();
  Card carta2 = baralhoPoker.comprar();
  Card carta3 = baralhoPoker.comprar();
  Card carta4 = baralhoPoker.comprar();
  Card carta5 = baralhoPoker.comprar();
  print(carta1);
  print(carta2);
  print(carta3);
  print(carta4);
  print(carta5);
  print("Numero de Cartas Restantes: ${baralhoPoker.cartasRestantes()}");

}

class Card{
  Card({required this.naipe, required this.valor});
  Naipe naipe;
  Valor valor;

  @override
  String toString(){return ("${valor.name} de ${naipe.name}");}
}

class Baralho{
  Baralho(){
    deck = criarBaralho();
  }
  List<Card> deck = [];

  void embaralhar(){
    deck.shuffle();
  }

  Card comprar(){
    Card cartaComprada = deck.first;
    deck.remove(cartaComprada);
    return cartaComprada;
  }

  int cartasRestantes(){
    int cartasRestantes = deck.length;
    return cartasRestantes;
  }

  List<Card> criarBaralho(){
    List<Card> lista = [];
    for(Naipe naipe in Naipe.values){
      for(Valor valor in Valor.values){
        Card carta = Card(naipe: naipe, valor: valor);
        lista.add(carta);
      }
    }
    return lista;
  }
}
