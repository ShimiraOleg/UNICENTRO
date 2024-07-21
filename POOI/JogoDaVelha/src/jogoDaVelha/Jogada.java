package jogoDaVelha;
import entradaDados.Console;
import java.util.InputMismatchException;

/**
 Código que rege as jogadas (se elas são validas e onde elas vão)
 @version 1.0
 @author Mateus de Oliveira Lopes
 */
public class Jogada {
    private static int posicao;
    /**
     * Determina o que acontece quando uma jogada é feita.
     * @param tabuleiro o tabuleiro sendo usado.
     * @param jogador o jogador dessa rodada.
     * @param turnoJogador1 determina se é o turno do jogador 1.
     * @param mJ o modo de jogo.
     * @return Uma boolean que determina se é ou não o turno do jogador 1.
     * @exception InvalidValueException se a entrada não for um valor inteiro aceito.
     * @exception InvalidPositionException se a posição do tabuleiro definida pela entrada já tem um valor dentro.
     * @exception InputMismatchException se a entrada não for um inteiro.
     */
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
            return turnoJogador1;
        } catch (InvalidValueException exc) {
            System.err.println(exc);
            return !(turnoJogador1);
        } catch (InvalidPositionException exc) {
            /* FUNCIONALIDADE EXTRA
             * Aqui é implementado a lógica da funcionalidade extra, cujo é um modo de jogo alternativo.
             * Nesse modo, cada jogador tem três trocas, que podem ser usadas para troca um 'X' por 'O' e vice versa.
             * A cada uso dessas trocas, a quantidade de usos restantes é decrementada do jogador.
             * Caso o jogador tenha zero trocas restantes, ele não pode fazer mais trocas.
             * Escolhemos usar essa funcionalidade extra pois ela faria proveito da ExceptionClass InvalidPositionException, assim a tornando mais fácil de implementar.
             * Além disso, ao criar um modo extra de jogo, adicionamos rejogabilidade no programa, assim o tornando mais interessante
             *
             * O gatilho pra começar essa funcionalidade é o mesmo do InvalidPositionException (colocar uma peça onde já tem outra), então ela é implementada em conjunto.
             */
            if(mJ == 0) //Caso o modo de jogo seja zero (que é o jogo da velha normal), ele só printa a mensagem de erro normal e não é feita a troca de turno
            {
                System.err.println(exc);
                return turnoJogador1 = !(turnoJogador1);
            }
            else if (mJ == 1 && jogador.getTrocas() > 0 && tabuleiro.getTabuleiro()[posicao - 1] != jogador.getSimbolo())
            //Caso o modo de jogo seja um (que é o modo alternativo), o jogador tenha trocas e a peça no tabuleiro seja diferente do simbolo do jogador,
            //a troca das peças é realizada e é feita a troca de turno
            {
                tabuleiro.getTabuleiro()[posicao - 1] = jogador.getSimbolo();
                jogador.setTrocas(jogador.getTrocas()-1);
                System.out.println("Jogador (" + jogador.getSimbolo() +") tem mais " + jogador.getTrocas() + " trocas disponiveis") ;
                return turnoJogador1 = turnoJogador1;
            }
            else if (tabuleiro.getTabuleiro()[posicao - 1] == jogador.getSimbolo())
            //Caso o simbolo do jogador seja o mesmo da peça no tabuleiro, é dito que a peça é igual a simbolo do jogador e não é feita a troca de turno.
            {
                System.err.println("O espaço já possui o simbolo (" +jogador.getSimbolo()+")!") ;
                return turnoJogador1 = !(turnoJogador1);
            }
            else
            //Caso nada acima seja executado, significa que o jogador não tem mais trocas disponíveis.
            //Então, é dito que o jogador não tem mais trocas e não é feita a troca de turno.
            {
                System.err.println("Jogador (" + jogador.getSimbolo() +") não tem mais trocas disponiveis") ;
                return turnoJogador1 = !(turnoJogador1);
            }
        } catch (InputMismatchException exc) {
            System.err.println("Coordenada inválida!\nPor favor, insira uma coordenada válida (1-9)");
            return turnoJogador1 = !(turnoJogador1);
        }
    }
}
