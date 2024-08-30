public class ContaBancaria {
    private int saldo;

    ContaBancaria()
    {
        saldo = 1000;
    }

    public void sacar()
    {
        saldo -= 200;
    }

    public void depositar()
    {
        saldo += 200;
    }

    public int getSaldo() {
        return saldo;
    }
}
