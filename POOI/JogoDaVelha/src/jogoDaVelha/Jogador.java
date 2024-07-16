/*
Código que rege os jogadores
@version 0.5
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;
public class Jogador {
  private String simbolo; // pode ser 'X' ou 'O'
  private String nome;
  private int pontos;

  public Jogador()
  {
    pontos = 0;
  }

  public Jogador(String simbolo, String nome) {
    this.simbolo = simbolo;
    this.nome = nome;
    pontos = 0;
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
}

