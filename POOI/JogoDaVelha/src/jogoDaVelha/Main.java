/*
Main que junta todos os .java
@version 0.65
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

import entradaDados.Console;

public class Main {
    public static void main(String[] args) {
        Jogador jAtual = new Jogador();
        Jogo jogo = new Jogo();
        boolean isJogando = true;

        String nome = Console.escolherNome('X');
        Jogador j1 = new Jogador("X", nome);
        nome = Console.escolherNome('O');
        Jogador j2 = new Jogador("O", nome);

        while (isJogando)
        {
            jogo.jogando(j1,j2,jAtual);
            jogo.mostrarPontuacao(j1,j2);
            char escolha = Console.jogarNovamente();
            isJogando = continuar(isJogando, jogo, escolha);
        }
    }

    public static boolean continuar(boolean isJogando, Jogo jogo, char escolha)
    {
        if(escolha == 'Y' || escolha == 'y')
        {
            isJogando = true;
            jogo.reiniciar();
        }
        else
        {
            isJogando = false;
        }
        return isJogando;
    }

}
