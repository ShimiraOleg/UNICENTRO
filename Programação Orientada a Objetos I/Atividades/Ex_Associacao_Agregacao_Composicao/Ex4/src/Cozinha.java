public class Cozinha {
    private Geladeira geladeira;
    private Microondas microondas;
    private Liquidificador liquidificador;

    public Cozinha(Geladeira geladeira, Microondas microondas, Liquidificador liquidificador)
    {
        this.geladeira = geladeira;
        this.microondas = microondas;
        this.liquidificador = liquidificador;
    }

    public void ligar()
    {
        geladeira.ligar();
        microondas.ligar();
        liquidificador.ligar();
    }

    public void desligar()
    {
        geladeira.desligar();
        microondas.desligar();
        liquidificador.desligar();
    }
}
