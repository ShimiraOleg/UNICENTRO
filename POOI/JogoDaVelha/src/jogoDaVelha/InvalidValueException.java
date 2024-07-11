/*
Código da exceção de quando o valor não está entre 1 e 9
@version 0.5
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;

public class InvalidValueException extends Exception{
    InvalidValueException()
    {

    }
    public String toString()
    {
        return "A coordenada inserida não está presente no tabuleiro!\nPor favor, insira uma coordenada válida (1-9)";
    }
}
