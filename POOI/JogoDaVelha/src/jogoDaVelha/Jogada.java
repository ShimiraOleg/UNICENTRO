package jogoDaVelha;
//import Jogador;
import entradaDados.Console;

public class Jogada {
  public static void jogada(String[] tabuleiro, Jogador jogador) {
    int posicao = Console.receberEntradaJogada();
    tabuleiro[posicao] = jogador.getSimbolo();
  }
}
