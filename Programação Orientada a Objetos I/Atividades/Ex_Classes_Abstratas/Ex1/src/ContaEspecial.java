public class ContaEspecial extends ContaBancaria{
    private double adcional;
    ContaEspecial(String nome1, double adcional)
    {
        super(nome1);
        this.adcional = adcional;
    }

    public void retira(double valor)
    {
        if(valor > (getSaldo()+adcional))
        {
            System.out.println("Valor excede o saldo disponivel mais o adcional! (R$ ("+(getSaldo()+" + "+adcional)+"))\nSaque de R$"+valor+" impossivel\n");
        }
        else if (valor <= (getSaldo()+adcional))
        {
            setSaldo(getSaldo() - valor);
            System.out.println("Saque de R$"+valor+" realizado com sucesso!\nSaldo Atual: R$" + getSaldo() + "\n");
        }
    }
}