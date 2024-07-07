package jogoDaVelha;

public class Tabuleiro extends Jogo{
    private String[] tabuleiro = new String[9];
    private int rodadas = 0;

    public String[] getTabuleiro() {
        return tabuleiro;
    }

    
    public void setTabuleiro(String tabuleiro, int i) {
        this.tabuleiro[i] = tabuleiro;
    }

    public void setRodadas()
    {
        rodadas++;
    }

    public int getRodadas()
    {
        return rodadas;
    }
}
