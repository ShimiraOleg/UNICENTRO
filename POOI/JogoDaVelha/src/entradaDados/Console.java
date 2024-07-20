/*
Classe que printa o tabuleiro e recebe entradas do usuário
@version 0.9
@author Mateus de Oliveira Lopes e Yan
 */
package entradaDados;
import jogoDaVelha.InvalidValueException;
import jogoDaVelha.Jogador;
import jogoDaVelha.Jogo;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Console {
  /*
   * Escreve no console o tabuleiro.
   * @param Strin[] tabuleiro O tabuleiro que vai ser escrito.
   */
  public static void printTabuleiro(String[] tabuleiro) {
    System.out.println(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8]);
  }

  /*
   * Recebe do usuário o nome do jogador.
   * @param char sin O simbolo desse jogador.
   * @return A string lida pelo console.
   */
  public static String escolherNome(char sin)
  {
    System.out.println("Insira o nome do jogador de (" + sin +")");
    Scanner scanner = new Scanner(System.in);
    String nome = scanner.next().toString();
    return nome;
  }

  /*
   * Recebe do usuário um valor de uma posição do tabuleiro.
   * @return O inteiro lido pelo console.
   */
  public static int receberEntradaJogada(){
    System.out.println("Digite a posição que deseja jogar: ");
    Scanner scanner = new Scanner(System.in);
    int posicao = scanner.nextInt();
    return posicao;
  }

  /*
   * Recebe do usuário um char que define se ele quer jogar novamente.
   * @return O character lido pelo console.
   */
  public static char jogarNovamente()
  {
    System.out.println("\nAperte 'Y' caso queira jogar novamente ");
    Scanner scanner = new Scanner(System.in);
    char escolha = scanner.next().charAt(0);
    return escolha;
  }

  /*
   * Recebe do usuário um int que define qual opção do menu ele escolheu.
   * @return O inteiro lido pelo console ou -1 se não for um inteiro válido.
   * @exception InputMismatchException se a entrada não for um numero inteiro.
   */
  public static int Menu(){
    try {
      System.out.println("1 - JOGAR PARTIDA\n2 - VER PLACAR GERAL\n3 - SAIR");
      Scanner scanner = new Scanner(System.in);
      int escolha = scanner.nextInt();
      if(escolha > 4 || escolha < 1)
      {
        return -1;
      }
      return escolha;
    } catch (InputMismatchException exc){
      System.out.println("Escolha inválida!\nPor favor, escolha uma das opções abaixo:");
      return 0;
    }
  }

  /*
   * Recebe do usuário um char que define o modo de jogo.
   * @param int modoJogo o modo de jogo.
   * @return Um inteiro escolhido com base no input do usuário.
   */
  public static int escolhaModoJogo(int modoJogo)
  {
    System.out.println("Digite '1' para jogar modo facil, '2' para jogar modo tryhard");
    Scanner scanner = new Scanner(System.in);
    char escolha2 = scanner.next().charAt(0);
    if(escolha2 == '1'){
      modoJogo = 0;
    } else if(escolha2 == '2'){
      modoJogo = 1;
    }
    return modoJogo;
  }

  /*
   * Recebe do usuário um char que define se ele quer jogar novamente.
   * @param boolean isJogando variavel que determina se o jogo continua ou não, Jogo jogo, char escolha, Jogador j1 e j2.
   * @return O character lido pelo console.
   */
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
  /*
   * Mostra a pontuação atual dos dois jogadores
   * @param Jogador j1 O jogador 1, Jogador j2 O jogador 2.
   */
  public void mostrarPontuacao(Jogador j1, Jogador j2)
  {
    System.out.println("\nPontuação de " + j1.getNome() + " (" + j1.getSimbolo() + "):\n" + j1.getPontos());
    System.out.println("Pontuação de " + j2.getNome() + " (" + j2.getSimbolo() + "):\n" + j2.getPontos());
  }
}
