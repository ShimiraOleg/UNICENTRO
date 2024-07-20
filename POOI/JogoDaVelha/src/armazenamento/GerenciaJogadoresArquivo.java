package armazenamento;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class GerenciaJogadoresArquivo implements GerenciaJogadores {

  private static String nomeDoArquivo;

  public GerenciaJogadoresArquivo(String nomeDoArquivo) {
    this.nomeDoArquivo = nomeDoArquivo;
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

  @Override 
  public void adicionarJogador(String nome1, int pontuacao1) {
  
  }

  public void adicionarJogador(String nome1, int pontuacao1, FileWriter fw) {
    try {
      fw.write(nome1 + " " + pontuacao1 + "\n");
      fw.flush();
    } catch (IOException e) {
      System.out.println("Erro ao adicionar jogador.");
    }
  }

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

  public static Map<String, Integer> criarMapaDoArquivo() {
    Map<String, Integer> mapa = new TreeMap<>();
    try (BufferedReader br = new BufferedReader(new FileReader(nomeDoArquivo))) {
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

  public void criarArquivoFinal() {
    Map<String, Integer> mapa = criarMapaDoArquivo();
    try (BufferedWriter bw = new BufferedWriter(new FileWriter("arquivoFinal.txt" , false))) {
      for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
        bw.write(entry.getKey() + " " + entry.getValue() + "\n");
      }
      bw.flush();
    } catch (IOException e) {
      System.out.println("Erro ao criar o arquivo final.");
    }
  }

  public void printarPontosGerais(){
    Map<String, Integer> mapa = criarMapaDoArquivo();
    for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
      System.out.println(entry.getKey() + " " + entry.getValue());
    }
  }
}