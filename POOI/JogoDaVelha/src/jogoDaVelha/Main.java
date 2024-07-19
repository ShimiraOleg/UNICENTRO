/*
Main que junta todos os .java
@version 0.8
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

import entradaDados.Console;
import armazenamento.DadosArray;
import java.io.FileWriter;
import java.util.ArrayList;
import armazenamento.GerenciaJogadoresArquivo;
import armazenamento.GerenciaJogadoresArrayList;

public class Main {
    public static void main(String[] args) {
        Jogador jAtual = new Jogador();
        Jogo jogo = new Jogo();
        GerenciaJogadoresArquivo gerencia = new GerenciaJogadoresArquivo("dadosArmazenados.txt");
        GerenciaJogadoresArrayList gerenciaArray = new GerenciaJogadoresArrayList();
        FileWriter fw = gerencia.criarArquivo(true);
        boolean isJogando = true;
        boolean isRodando = true;
        int modoJogo = 0;
        ArrayList<DadosArray> array = new ArrayList<DadosArray>();
        
        if(isJogando == true){
        while(isRodando){
            switch (Console.escolhaMenu()) {
                case 1: // jogar
                    modoJogo = Console.escolhaModoJogo(modoJogo);
                    System.out.println("Modo Jogo: " + modoJogo);
                    isRodando = false;
                    isJogando = true;
                    break;
                case 2: // leaderboard
                    //gerencia.printarPontosGerais();
                    gerenciaArray.atualizarJogador(array);
                    //System.out.println(array);
                    gerenciaArray.printarPontosGerais(array);
                    isJogando = false;
                    break;
                case 3: // sair
                    isRodando = false;
                    isJogando = false;
                    break;
                default:
                    isJogando = false;
                    System.out.println("Ta tirando amostradinho");
                    break;
            }
            Jogador j1 = new Jogador("X", null);
            Jogador j2 = new Jogador("O", null);

            if(isJogando == true){
                j1.setNome(Console.escolherNome('X'));
                j2.setNome(Console.escolherNome('O'));
            }

            while (isJogando)
            {
                jogo.jogando(j1,j2,jAtual, modoJogo);
                jogo.mostrarPontuacao(j1,j2);
                char escolha = Console.jogarNovamente();
                isJogando = continuar(isJogando, jogo, escolha, j1, j2);
                if(!isJogando) {
                    
                    //gerenciaArray.atualizarJogador(array);
                    gerencia.adicionarJogador(j1.getNome(), j1.getPontos(), fw);
                    gerencia.adicionarJogador(j2.getNome(), j2.getPontos(), fw);
                    gerenciaArray.atualizarJogador(array);
                }
                isRodando = !isJogando;
            }
            } 
        }
        System.out.println("Fim do programa");
        
    }
        
    
    public static boolean continuar(boolean isJogando, Jogo jogo, char escolha, Jogador j1, Jogador j2)
    {
        if(escolha == 'Y' || escolha == 'y')
        {
            isJogando = true;
        }
        else
        {
            isJogando = false;
        }
        jogo.reiniciar(j1,j2);
        return isJogando;
    }

}
