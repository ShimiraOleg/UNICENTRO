public class ContaBanco {
    private int numConta;
    private double saldo;

    public ContaBanco(int numConta) {
        this.numConta = numConta;
        saldo = 0;
    }

    public ContaBanco(int numConta, double saldo) {
        this.numConta = numConta;
        this.saldo = saldo;
    }

    public int getNumConta() {
        return numConta;
    }

    public void deposito(double valor) {
        saldo += valor;
    }

    public void saque(double valor) {
        saldo -= valor;
    }

    public double getSaldo() {
        return saldo;
    }

    @Override
    public String toString() {
        return "ContaBanco [numConta = " + numConta + ", saldo = " + saldo + "]";
    }

}