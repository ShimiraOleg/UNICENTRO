/*
Main que junta todos os .java
@version 0.7
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
        //GerenciaJogadoresArquivo gerencia2 = new GerenciaJogadoresArquivo("arquivoFinal.txt");
        GerenciaJogadoresArrayList gerenciaArray = new GerenciaJogadoresArrayList();
        FileWriter fw = gerencia.criarArquivo(true);
        boolean isJogando = true;
        boolean isRodando = true;
        int modoJogo = 1;
        ArrayList<DadosArray> array = new ArrayList<DadosArray>();
        //
        while(isRodando){
            switch (Console.escolha(modoJogo)) {
                case 1: // jogar
                    isRodando = false;
                    break;
                case 2: // leaderboard
                    gerencia.printarPontosGerais();
                    break;
                case 3: // sair
                    isRodando = false;
                    isJogando = false;
                    break;
                default:
                    System.out.println("Ta tirando amostradinho");
                    break;
            }
            }
            if(isJogando == true){
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
            gerenciaArray.atualizarJogador(array, j1.getNome(), j1.getPontos());
            gerenciaArray.atualizarJogador(array, j2.getNome(), j2.getPontos());
            gerencia.adicionarJogador(j1.getNome(), j1.getPontos(), fw);
            gerencia.adicionarJogador(j2.getNome(), j2.getPontos(), fw);
            }
            //gerencia.criarArquivoFinal();
        }
        //gerencia2.printarPontosGerais();
        //System.out.println(gerencia.criarMapaDoArquivo());
        //System.out.println(array);
    
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
