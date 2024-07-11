/*
Main que junta todos os .java
@version 0.6
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

import entradaDados.Console;

public class Main {
    public static void main(String[] args) {
        Jogador j1 = new Jogador("X", "Teste");
        Jogador j2 = new Jogador("O", "Testador");
        Jogador jAtual = new Jogador();
        Jogo jogo = new Jogo();
        boolean isJogando = true;


        while (isJogando)
        {
            jogo.jogando(j1,j2,jAtual);
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
