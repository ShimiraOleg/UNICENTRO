/*
Código que rege o tabuleiro
@version 0.5
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

public class Tabuleiro{
    private String[] tabuleiro = new String[9];
    private int rodadas = 0;

    /*
     * Construtor que inicializa o tabuleiro
     */
    public Tabuleiro()
    {
        for(int i = 0; i < 9; i++)
        {
            String s = String.valueOf(i+1);
            tabuleiro[i] = s;
        }
    }

    /*
     * Construtor que inicializa o tabuleiro
     * @return String[] tabuleiro O tabuleiro
     */
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

    public void setRodadas(int valor)
    {
        rodadas = valor;
    }

    public int getRodadas()
    {
        return rodadas;
    }
}
