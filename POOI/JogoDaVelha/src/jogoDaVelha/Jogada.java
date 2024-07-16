/*
Código que rege as jogadas (se elas são validas e onde elas vão)
@version 1.0
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;
import entradaDados.Console;
import java.util.InputMismatchException;

public class Jogada {
    private static int posicao;
    public static boolean jogada(Tabuleiro tabuleiro, Jogador jogador, boolean turnoJogador1, int mJ){
        try {
            posicao = Console.receberEntradaJogada();
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
            if(mJ == 0)
            {
                System.out.println(exc);
                return turnoJogador1 = !(turnoJogador1);
            }
            else if (mJ == 1 && jogador.getTrocas() > 0 && tabuleiro.getTabuleiro()[posicao - 1] != jogador.getSimbolo())
            {
                tabuleiro.getTabuleiro()[posicao - 1] = jogador.getSimbolo();
                jogador.setTrocas(jogador.getTrocas()-1);
                System.out.println("Jogador (" + jogador.getSimbolo() +") tem mais " + jogador.getTrocas() + " trocas disponiveis") ;
                return turnoJogador1 = turnoJogador1;
            }
            else if (tabuleiro.getTabuleiro()[posicao - 1] == jogador.getSimbolo())
            {
                System.out.println("O espaço já possui o simbolo (" +jogador.getSimbolo()+")!") ;
                return turnoJogador1 = !(turnoJogador1);
            }
            else
            {
                System.out.println("Jogador (" + jogador.getSimbolo() +") não tem mais trocas disponiveis") ;
                return turnoJogador1 = !(turnoJogador1);
            }
        } catch (InputMismatchException exc) {
            System.out.println("Coordenada inválida!\nPor favor, insira uma coordenada válida (1-9)");
            return turnoJogador1 = !(turnoJogador1);
        }
    }
}
