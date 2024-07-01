package jogoDaVelha;

public class Tabuleiro extends Jogo{
    private String[] tabuleiro = new String[9];

    public String[] getTabuleiro() {
        return tabuleiro;
    }

    public void setTabuleiro(String tabuleiro, int i) {
        this.tabuleiro[i] = tabuleiro;
    }
}
