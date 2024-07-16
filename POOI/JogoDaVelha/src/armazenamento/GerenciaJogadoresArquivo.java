package armazenamento;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;




public class GerenciaJogadoresArquivo implements GerenciaJogadores {
  private int contRodadas = 1;
  private String nomeDoArquivo;

  public GerenciaJogadoresArquivo(String nomeDoArquivo) {
    this.nomeDoArquivo = nomeDoArquivo;
    //this.contRodadas = contRodadas;
  }

  public void atualizarContRodadas() {
    this.contRodadas++;
  }

  public FileWriter criarArquivo(boolean append) {
    try {
      File arquivo = new File(nomeDoArquivo);
      FileWriter fw = new FileWriter(arquivo, append);
      System.out.println("Arquivo criado com sucesso!");
      return fw;
    } catch (IOException e) {
      System.out.println("Erro ao criar o arquivo.");
      return null;
    }
  }

  public void adicionarJogador(String nome1, int pontuacao1, String nome2, int pontuacao2, FileWriter fw) {
    try {
      //BufferedWriter bw = new BufferedWriter(fw);
      //bw.write(nome1 + " " + pontuacao1 + "\n" + nome2 + " " + pontuacao2);
      //bw.close();
      fw.write("--------------------------\n");
      fw.write("Jogo " + contRodadas + "\n");
      fw.write(nome1 + " " + pontuacao1 + "\n");
      fw.write(nome2 + " " + pontuacao2 + "\n");
      
      fw.flush();
    } catch (IOException e) {
      System.out.println("Erro1 ao adicionar jogador.");
    }
  }

}
