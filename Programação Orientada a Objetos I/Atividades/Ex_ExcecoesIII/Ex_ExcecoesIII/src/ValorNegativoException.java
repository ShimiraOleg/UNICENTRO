public class ValorNegativoException extends Exception{
    private double valor;

    public ValorNegativoException(double valor)
    {
        this.valor = valor;
    }

    @Override
    public String toString()
    {
        return "O valor que você quer sacar (R$ " + valor + ") é negativo, portando o saque não será possivel";
    }
}
