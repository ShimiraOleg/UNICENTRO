package jogoDaVelha;

public class Tabuleiro extends Jogo{
    private String[] tabuleiro = new String[9];
    private int rodadas = 0;

    public Tabuleiro()
    {
        for(int i = 0; i < 9; i++)
        {
            String s = String.valueOf(i+1);
            tabuleiro[i] = s;
        }
    }

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
