public class ContaCorrente {
    /** Saldo da conta corrente. */
    private double saldo;

    /** Retorna a taxa de operação da conta corrente */
    protected double getTaxaOperacao() {
        return 0.05;
    }

    /** Deposita uma quantia na conta corrente. */
    public void depositar(double quantia) throws ValorNegativoException {
        if (quantia < 0) throw new ValorNegativoException(quantia);
        saldo += quantia;
    }

    /** Saca uma quantia da conta corrente. */
    public void sacar(double quantia) throws ValorNegativoException, SaldoInsuficienteException {
        if (quantia < 0) throw new ValorNegativoException(quantia);
        quantia += getTaxaOperacao() * quantia;
        if (quantia > saldo) throw new SaldoInsuficienteException(quantia, saldo);
        saldo -= quantia;
    }

    /** Retorna o saldo da conta corrente. */
    public double getSaldo() {
        return saldo;
    }
}