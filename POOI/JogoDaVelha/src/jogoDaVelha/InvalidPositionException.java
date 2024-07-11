/*
Código da execeção de quando o lugar já tem uma peça e não pode ser colocado uma outra peça no lugar
@version 0.5
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

public class InvalidPositionException extends Exception{
    private int pos;
    private String sim;
    InvalidPositionException(int i, String j)
    {
        pos = i;
        sim = j;
    }
    public String toString()
    {
        return "A coordenada inserida (" + pos + ") já tem uma peça (" + sim + ")!\nPor favor, escolha outra coordenada" ;
    }
}
