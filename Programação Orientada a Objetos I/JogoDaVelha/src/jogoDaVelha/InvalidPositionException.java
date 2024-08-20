package jogoDaVelha;

/**
 Código da execeção de quando o lugar já tem uma peça e não pode ser colocado uma outra peça no lugar
 @version 0.5
 @author Mateus de Oliveira Lopes
 */
public class InvalidPositionException extends Exception{
    private int pos;
    private String sim;

    /**
     * O construtor da classe.
     * @param i A coordenada inserida.
     * @param j O simbolo do jogador.
     */
    InvalidPositionException(int i, String j)
    {
        pos = i;
        sim = j;
    }

    /**
     * Atualização do método toString para imprimir a mensagem desejada.
     * @return A mesagem desejada.
     */
    public String toString()
    {
        return "A coordenada inserida (" + pos + ") já tem uma peça (" + sim + ")!\nPor favor, escolha outra coordenada" ;
    }
}
