public abstract class ContaBancaria {
    private String nome;
    private double saldo;

    ContaBancaria(String nome1){
            nome = nome1;
    }

    public abstract void retira(double valor);

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void deposita(double valor)
    {
        saldo += valor;
    }
}
