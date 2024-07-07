package jogoDaVelha;

public class Jogador {
  char simbolo; // pode ser 'X' ou 'O'  
  String nome;

  public Jogador(char simbolo, String nome) {
    this.simbolo = simbolo;
    this.nome = nome;
  }
  public char getSimbolo() {
    return simbolo;
  }
  public void setSimbolo(char simbolo) {
    this.simbolo = simbolo;
  }
}

