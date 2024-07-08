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
        return "O valor inserido (" + pos + ") já tem uma peça (" + sim + ")!\nEscolha outra posição" ;
    }
}
