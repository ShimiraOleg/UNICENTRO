/*
Main que junta todos os .java
@version 0.7
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

import entradaDados.Console;

public class Main {
    public static void main(String[] args) {
        Jogador jAtual = new Jogador();
        Jogo jogo = new Jogo();
        boolean isJogando = true;
        int modoJogo = 1;

        String nome = Console.escolherNome('X');
        Jogador j1 = new Jogador("X", nome);
        nome = Console.escolherNome('O');
        Jogador j2 = new Jogador("O", nome);

        while (isJogando)
        {
            jogo.jogando(j1,j2,jAtual, modoJogo);
            jogo.mostrarPontuacao(j1,j2);
            char escolha = Console.jogarNovamente();
            isJogando = continuar(isJogando, jogo, escolha, j1, j2);
        }
    }

    public static boolean continuar(boolean isJogando, Jogo jogo, char escolha, Jogador j1, Jogador j2)
    {
        if(escolha == 'Y' || escolha == 'y')
        {
            isJogando = true;
            jogo.reiniciar(j1,j2);
        }
        else
        {
            isJogando = false;
        }
        return isJogando;
    }

}
