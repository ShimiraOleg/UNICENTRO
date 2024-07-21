package entradaDados;
import jogoDaVelha.Jogador;
import jogoDaVelha.Jogo;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 Classe que printa o tabuleiro e recebe entradas do usuário
 @version 1.0
 @author Mateus de Oliveira Lopes e Yan Gabriel Reis
 */
public class Console {
  /**
   * Escreve no console o tabuleiro.
   * @param tabuleiro O tabuleiro que vai ser escrito.
   */
  public static void printTabuleiro(String[] tabuleiro) {
    System.out.println(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5]);
    System.out.println("---+---+---");
    System.out.println(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8]);
  }

  /**
   * Recebe do usuário o nome do jogador.
   * @param sin O simbolo desse jogador.
   * @return A string lida pelo console.
   */
  public static String escolherNome(char sin)
  {
    System.out.println("Insira o nome do jogador de (" + sin +")");
    Scanner scanner = new Scanner(System.in);
    return scanner.next().toString();
  }

  /**
   * Recebe do usuário um valor de uma posição do tabuleiro.
   * @return O inteiro lido pelo console.
   */
  public static int receberEntradaJogada(){
    System.out.println("Digite a posição que deseja jogar: ");
    Scanner scanner = new Scanner(System.in);
    return scanner.nextInt();
  }

  /**
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

  /**
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

  /**
   * FUNCIONALIDADE EXTRA: Recebe do usuário um char que define o modo de jogo.
   * @param modoJogo o modo de jogo.
   * @return Um inteiro escolhido com base no input do usuário.
   */
  public static int escolhaModoJogo(int modoJogo)
  {
    do {
      System.out.println("ESCOLHA O MODO DE JOGO:\n1 - Modo Tradicional\n2 - Modo com Trocas");
      Scanner scanner = new Scanner(System.in);
      char escolha2 = scanner.next().charAt(0);
      if (escolha2 == '1') {
        modoJogo = 0;
      } else if (escolha2 == '2') {
        modoJogo = 1;
      } else {
        System.out.println("Escolha inválida!\nPor favor, escolha uma das opções abaixo:");
        modoJogo = -1;
      }
    } while (modoJogo != 0 && modoJogo != 1);
    return modoJogo;
  }

  /**
   * Função que determina se o jogo reinicia ou volta para o menu
   * @param jogo o jogo atual.
   * @param escolha a escolha do usuário.
   * @param j1 o jogador 1.
   * @param j2 o jogador 2.
   * @return uma boolean que define se o jogo reinicia ou volta para o menu
   */
  public static boolean continuar(Jogo jogo, char escolha, Jogador j1, Jogador j2)
  {
    if(escolha == 'Y' || escolha == 'y')
    {
      jogo.reiniciar(j1,j2);
      return true;
    }
    else
    {
      jogo.reiniciar(j1,j2);
      return false;
    }
  }

  /**
   * Função que imprime na tela a pontuação da partida atual
   * @param j1 o jogador 1
   * @param j2 o jogador 2
   */
  public void mostrarPontuacao(Jogador j1, Jogador j2)
  {
    System.out.println("\nPontuação de " + j1.getNome() + " (" + j1.getSimbolo() + "):\n" + j1.getPontos());
    System.out.println("Pontuação de " + j2.getNome() + " (" + j2.getSimbolo() + "):\n" + j2.getPontos());
  }
}
