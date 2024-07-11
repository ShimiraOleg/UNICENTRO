/*
Código que rege as jogadas (se elas são validas e onde elas vão)
@version 0.5
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;
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
              throw new InvalidPositionException(posicao, tabuleiro.getTabuleiro()[posicao -1]);
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
            System.out.println("Coordenada inválida!\nPor favor, insira uma coordenada válida (1-9)");
            return turnoJogador1 = !(turnoJogador1);
        }
    }
}
