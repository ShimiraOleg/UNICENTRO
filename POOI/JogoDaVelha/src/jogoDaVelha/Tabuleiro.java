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
     * Retorna o array do tabuleiro
     * @return String[] tabuleiro O tabuleiro
     */
    public String[] getTabuleiro() {
        return tabuleiro;
    }

    /*
     * adciona o valor recebido no tabuleiro na coordenada recebida
     * @param valor O valor a ser colocado na coordenada
     * @param i O valor referente a coordenada no vetor
     */
    public void setTabuleiro(String valor, int i) {
        this.tabuleiro[i] = valor;
    }

    /*
     * incrementa o valor de rodadas em 1
     */
    public void setRodadas()
    {
        rodadas++;
    }

    /*
     * atribui para rodadas o valor recebido
     * @param valor O valor recebido
     */
    public void setRodadas(int valor)
    {
        rodadas = valor;
    }

    /*
     * Retorna o valor de rodadas
     * @return String[] tabuleiro O tabuleiro
     */
    public int getRodadas()
    {
        return rodadas;
    }
}
