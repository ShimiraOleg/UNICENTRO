package armazenamento;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

/**
 Implementação da interface GerenciaJogadores para adicionar e atualizar jogadores em um arquivo de texto, além
 de salvar todos esses dados para serem acessados fora do tempo de execução.
 @version 1.0
 @author Yan Gabriel Reis Oliveira
 */
public class GerenciaJogadoresArquivo implements GerenciaJogadores {

  private String nomeDoArquivo;

  /**
   * Construtor da classe GerenciaJogadoresArquivo.
   */
  public GerenciaJogadoresArquivo(String nomeDoArquivo) {
    this.nomeDoArquivo = nomeDoArquivo;
  }

  /**
   * Este método cria um arquivo de texto.
   * @param append Boolean que determina se o arquivo será criado do zero ou se será adicionado ao final do arquivo.
   * @return FileWriter que é o arquivo criado.
   */
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

  @Override 
  public void adicionarJogador(String nome1, int pontuacao1) {
  
  }

  /**
   * Este método adiciona um jogador ao arquivo de texto.
   * @param nome1 String que é o nome do jogador.
   * @param pontuacao1 int que é a pontuação do jogador.
   * @param fw FileWriter que é o arquivo onde os dados serão adicionados.
   * @return void
   */
  public void adicionarJogador(String nome1, int pontuacao1, FileWriter fw) {
    try {
      fw.write(nome1 + " " + pontuacao1 + "\n");
      fw.flush();
    } catch (IOException e) {
      System.out.println("Erro ao adicionar jogador.");
    }
  }

  /**
   * Este método atualiza a pontuação de um jogador no arquivo de texto.
   * @param nome1 String que é o nome do jogador.
   * @param pontuacao1 int que é a pontuação do jogador.
   * @param fw FileWriter que é o arquivo onde os dados serão atualizados.
   * @return void
   */
  public void atualizarJogador(String nome1, int pontuacao1, FileWriter fw) {
    Map<String, Integer> mapa = criarMapaDoArquivo();
    if (mapa.containsKey(nome1)) {
      int pontuacaoAtual = mapa.get(nome1);
      pontuacaoAtual += pontuacao1;
      mapa.put(nome1, pontuacaoAtual);
    } else {
      mapa.put(nome1, pontuacao1);
    }

    try {
      fw.write("");
      for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
        fw.write(entry.getKey() + " " + entry.getValue() + "\n");
      }
      fw.flush();
    } catch (IOException e) {
      System.out.println("Erro ao atualizar jogador.");
    }
  }

  /**
   * Este método cria um mapa a partir do arquivo de texto.
   * @return Map<String, Integer> que é o mapa criado.
   */
  public static Map<String, Integer> criarMapaDoArquivo() {
    Map<String, Integer> mapa = new TreeMap<>();
    try (BufferedReader br = new BufferedReader(new FileReader("dadosArmazenados.txt"))) {
      String linha;
      while ((linha = br.readLine()) != null) {
        String[] partes = linha.split(" ", 2);
        if (partes.length >= 2) {
          String chave = partes[0];
          int valor = Integer.parseInt(partes[1]);
          if (mapa.containsKey(chave)) {
            int pontuacaoAtual = mapa.get(chave);
            pontuacaoAtual += valor;
            mapa.put(chave, pontuacaoAtual);
          } else {
            mapa.put(chave, valor);
          }
        }
      }
    } catch (IOException e) {
      System.out.println("Erro ao ler o arquivo.");
    }
    return mapa;
  }

  
  /**
   * Este método imprime os pontos gerais dos jogadores.
   * @return void
   */
  public void printarPontosGerais(){
    Map<String, Integer> mapa = criarMapaDoArquivo();
    for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
      System.out.println(entry.getKey() + " " + entry.getValue());
    }
  }
}