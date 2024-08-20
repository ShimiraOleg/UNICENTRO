public class ContaSimples extends ContaBancaria {
    ContaSimples(String nome1)
    {
        super(nome1);
    }

    public void retira(double valor)
    {
        if(valor > getSaldo())
        {
            System.out.println("Valor exede o saldo disponivel! (R$"+ getSaldo() +")\nSaque de R$"+valor+" impossivel\n");
        }
        else if (valor <= getSaldo())
        {
            setSaldo(getSaldo() - valor);
            System.out.println("Saque de R$"+ valor +" realizado com sucesso!\nSaldo Atual: R$" + getSaldo() + "\n");
        }
    }
}
