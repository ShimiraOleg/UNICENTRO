package jogoDaVelha;

public class Jogador {
  String simbolo; // pode ser 'X' ou 'O'
  String nome;

  public Jogador()
  {

  }

  public Jogador(String simbolo, String nome) {
    this.simbolo = simbolo;
    this.nome = nome;
  }
  public String getSimbolo() {
    return simbolo;
  }
  public void setSimbolo(String simbolo) {
    this.simbolo = simbolo;
  }
}

