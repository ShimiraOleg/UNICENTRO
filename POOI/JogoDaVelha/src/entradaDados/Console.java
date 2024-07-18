/*
Código que printa o tabuleiro e recebe a entrada do usuário
@version 0.65
@author Mateus de Oliveira Lopes
 */
package entradaDados;
import java.util.InputMismatchException;
import java.util.Scanner;
import armazenamento.GerenciaJogadoresArquivo;

public class Console {
  public static void printTabuleiro(String[] tabuleiro) {
    System.out.println(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8]);
  }

  public static String escolherNome(char sin)
  {
    System.out.println("Insira o nome do jogador de (" + sin +")");
    Scanner scanner = new Scanner(System.in);
    String nome = scanner.next().toString();
    return nome;
  }

  public static int receberEntradaJogada(){
    System.out.println("Digite a posição que deseja jogar: ");
    Scanner scanner = new Scanner(System.in);
    int posicao = scanner.nextInt();
    return posicao;
  }

  public static char jogarNovamente()
  {
    System.out.println("\nAperte 'Y' caso queira jogar novamente ");
    Scanner scanner = new Scanner(System.in);
    char escolha = scanner.next().charAt(0);
    return escolha;
  }
  /*/
  public static boolean printarPontosGerais(){
      System.out.println("Digite 'P' para ver os pontos gerais, 'Y' para jogar");
      Scanner scanner = new Scanner(System.in);
      char escolha = scanner.next().charAt(0);
      if(escolha == 'P' || escolha == 'p'){
        GerenciaJogadoresArquivo gerencia = new GerenciaJogadoresArquivo("arquivoFinal.txt");
        gerencia.printarPontosGerais();
        return true;
      } else if(escolha == 'Y' || escolha == 'y'){
        return false;
      }
      return true;
  }
      */

  public static int escolha(int modoJogo){
    System.out.println("Digite 'P' para ver os pontos gerais, 'Y' para jogar, 'S' para sair");
    Scanner scanner = new Scanner(System.in);
    char escolha = scanner.next().charAt(0);
    if(escolha == 'P' || escolha == 'p'){
      return 2;
    } else if(escolha == 'Y' || escolha == 'y'){
      System.out.println("Digite '1' para jogar modo facil, '2' para jogar modo tryhard");
      char escolha2 = scanner.next().charAt(0);
      if(escolha2 == '1'){
        modoJogo = 1;
      } else if(escolha2 == '2'){
        modoJogo = 2;
      }
      return 1;
    } else if(escolha == 'S' || escolha == 's'){
      return 3;
    }
    return 0;
  }
}
