package jogoDaVelha;

/**
 Código da exceção de quando o valor não está entre 1 e 9.
 @version 0.5
 @author Mateus de Oliveira Lopes.
 */
public class InvalidValueException extends Exception{
    /**
     * O construtor da classe
     */
    InvalidValueException()
    {

    }
    /**
     * Atualização do método toString para imprimir a mensagem desejada.
     * @return A mesagem desejada.
     */
    public String toString()
    {
        return "A coordenada inserida não está presente no tabuleiro!\nPor favor, insira uma coordenada válida (1-9)";
    }
}
