/*
Código que rege os jogadores
@version 0.9
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;
public class Jogador {
  private String simbolo; // pode ser 'X' ou 'O'
  private String nome;
  private int pontos, trocas; //FUNCIONALIDADE EXTRA: na Classe Jogador é salvo a quantidade de trocas que ele possui, sendo usado o get e set para altera-las.

  public Jogador()
  {
    pontos = 0;
    trocas = 3; //As trocas são inicializadas sempre como 3.
  }

  public Jogador(String simbolo, String nome) {
    this.simbolo = simbolo;
    this.nome = nome;
    pontos = 0;
    trocas = 3; //As trocas são inicializadas sempre como 3.
  }
  public String getSimbolo() {
    return simbolo;
  }

  public void setSimbolo(String simbolo) {
    this.simbolo = simbolo;
  }

  public String getNome()
  {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public int getPontos() {
    return pontos;
  }

  public void setPontos(int pontos) {
    this.pontos = pontos;
  }

  public void setTrocas(int trocas) {
    this.trocas = trocas;
  }

  public int getTrocas(){
    return trocas;
  }
}

