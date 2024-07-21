package jogoDaVelha;

/**
 Código que rege os jogadores
 @version 0.9
 @author Mateus de Oliveira Lopes
 */
public class Jogador {
  private String simbolo; // pode ser 'X' ou 'O'
  private String nome;
  private int pontos, trocas; //FUNCIONALIDADE EXTRA: na Classe Jogador é salvo a quantidade de trocas que ele possui, sendo usado o get e set para altera-las.

  /**
   * Construtor que inicializa o jogador
   */
  public Jogador()
  {
    pontos = 0;
    trocas = 3; //As trocas são inicializadas sempre como 3.
  }

  /**
   * Construtor que inicializa o jogador
   * @param simbolo O simbolo do jogador
   * @param nome O nome do jogador
   */
  public Jogador(String simbolo, String nome) {
    this.simbolo = simbolo;
    this.nome = nome;
    pontos = 0;
    trocas = 3; //As trocas são inicializadas sempre como 3.
  }

  /**
   * retorna o simbolo do jogador
   * @return o valor do simbolo
   */
  public String getSimbolo() {
    return simbolo;
  }

  public void setSimbolo(String simbolo) {
    this.simbolo = simbolo;
  }

  /**
   * retorna o nome do jogador
   * @return o valor do nome
   */
  public String getNome()
  {
    return nome;
  }

  /**
   * atribui para nome o valor recebido
   * @param nome O nome recebido
   */
  public void setNome(String nome) {
    this.nome = nome;
  }

  /**
   * retorna os pontos do jogador
   * @return o valor dos pontos
   */
  public int getPontos() {
    return pontos;
  }

  /**
   * atribui para pontos o valor recebido
   * @param pontos O valor de pontos recebido
   */
  public void setPontos(int pontos) {
    this.pontos = pontos;
  }

  /**
   * retorna a quantidade de trocas do jogador
   * @return o valor de trocas
   */
  public int getTrocas(){
    return trocas;
  }

  /**
   * atribui para trocas o valor recebido
   * @param trocas O valor de trocas recebido
   */
  public void setTrocas(int trocas) {
    this.trocas = trocas;
  }
}

