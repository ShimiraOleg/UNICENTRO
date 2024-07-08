package jogoDaVelha;

public class InvalidValueException extends Exception{
    InvalidValueException()
    {

    }
    public String toString()
    {
        return "O valor inserido não é válido!\nPor favor, escreva um valor válido";
    }
}
