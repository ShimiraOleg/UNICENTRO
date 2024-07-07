package entradaDados;
import jogoDaVelha.Jogador;
import java.util.Scanner;

public class Console {
  public static void printTabuleiro(String[] tabuleiro) {
    System.out.println(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8]);
  }



  public static void jogada(String[] tabuleiro, Jogador jogador){  
    System.out.println("Digite a posição que deseja jogar: ");
    Scanner scanner = new Scanner(System.in);
    int posicao = scanner.nextInt();
    tabuleiro[posicao] = jogador.getSimbolo();
    scanner.close();
  }
}
