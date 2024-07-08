package jogoDaVelha;
//import Jogador;
import com.sun.jdi.InvalidTypeException;
import entradaDados.Console;

import java.util.InputMismatchException;

public class Jogada {
  public static boolean jogada(Tabuleiro tabuleiro, Jogador jogador, boolean turnoJogador1){
    try {
      int posicao = Console.receberEntradaJogada();
      if(posicao - 1 < 0 || posicao - 1 > 8)
      {
        throw new InvalidValueException();
      }
      if(tabuleiro.getTabuleiro()[posicao -1] == "X" || tabuleiro.getTabuleiro()[posicao -1] == "O")
      {
        throw new InvalidPositionException(posicao-1, jogador.getSimbolo());
      }
      tabuleiro.getTabuleiro()[posicao - 1] = jogador.getSimbolo();
      tabuleiro.setRodadas();
      return turnoJogador1 = turnoJogador1;
    } catch (InvalidValueException exc) {
      System.out.println(exc);
      return turnoJogador1 = !(turnoJogador1);
    } catch (InvalidPositionException exc) {
      System.out.println(exc);
      return turnoJogador1 = !(turnoJogador1);
    } catch (InputMismatchException exc) {
      System.out.println("Valor inválido!\nExcreva um valor válido (1-9)");
      return turnoJogador1 = !(turnoJogador1);
    }
  }
}
