public class AppCozinha {
    public static void main(String[] args) {
        Geladeira geladeira = new Geladeira();
        Microondas microondas = new Microondas();
        Liquidificador liquidificador = new Liquidificador();

        Cozinha cozinha = new Cozinha(geladeira,microondas,liquidificador);

        cozinha.ligar();
        geladeira.observar();
        microondas.observar();
        liquidificador.observar();

        System.out.println();

        cozinha.desligar();
        geladeira.observar();
        microondas.observar();
        liquidificador.observar();
    }
}
