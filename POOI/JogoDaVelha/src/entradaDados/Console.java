/*
Código que printa o tabuleiro e recebe a entrada do usuário
@version 0.6
@author Mateus de Oliveira Lopes
 */
package entradaDados;
import java.util.Scanner;

public class Console {
  public static void printTabuleiro(String[] tabuleiro) {
    System.out.println(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8]);
  }

  public static int receberEntradaJogada(){  
    System.out.println("Digite a posição que deseja jogar: ");
    Scanner scanner = new Scanner(System.in);
    int posicao = scanner.nextInt();
    return posicao;
  }

  public static char jogarNovamente()
  {
    System.out.println("\nDeseja jogar novamente? (y/n)");
    Scanner scanner = new Scanner(System.in);
    char escolha = scanner.next().charAt(0);
    return escolha;
  }
}
