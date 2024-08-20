public class EletroApp {
    public static void main(String[] args) {
        Eletro[] eletros = new Eletro[2];
        eletros[0] = new Geladeira();
        eletros[1] = new Microondas();

        acionar(eletros);
    }

    public static void acionar(Eletro[] eletros) {
        for (Eletro eletro: eletros)
        {
            eletro.ligar();
            eletro.desligar();
        }
    }
}
