/*
Main que junta todos os .java
@version 0.65
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

import entradaDados.Console;

import java.io.FileWriter;

import armazenamento.GerenciaJogadoresArquivo;

public class Main {
    public static void main(String[] args) {
        Jogador jAtual = new Jogador();
        Jogo jogo = new Jogo();
        GerenciaJogadoresArquivo gerencia = new GerenciaJogadoresArquivo("dadosArmazenados.txt");
        FileWriter fw = gerencia.criarArquivo(true);
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
            gerencia.adicionarJogador(j1.getNome(), j1.getPontos(),j2.getNome(), j2.getPontos(), fw);
            gerencia.atualizarContRodadas();
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
