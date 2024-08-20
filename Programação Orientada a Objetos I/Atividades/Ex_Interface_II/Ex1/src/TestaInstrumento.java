public class TestaInstrumento {
    public static void main(String[] args) {
        Instrumento[] instrumentos = new Instrumento[5];
        instrumentos[0] = new Sopro();
        instrumentos[1] = new SoproMetal();
        instrumentos[2] = new SoproMadeira();
        instrumentos[3] = new Percussao();
        instrumentos[4] = new Corda();

        teste(instrumentos);

    }

    public static void teste(Instrumento[] instrumentos) {
        for(Instrumento instrumento: instrumentos)
        {
            instrumento.nome();
            instrumento.afinar();
            instrumento.tocar();
            System.out.println();
        }
    }
}


