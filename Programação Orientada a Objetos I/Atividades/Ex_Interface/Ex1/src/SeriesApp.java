public class SeriesApp {
    public static void main(String[] args) {
        Series[] vetorSeries = new Series[2]; //polimorfismo
        MaisDois s1 = new MaisDois();
        MaisTres s2 = new MaisTres();

        vetorSeries[0] = s1;
        vetorSeries[1] = s2;

        imprime(vetorSeries);
    }

    public static void imprime(Series[] series) {
        for (Series serie: series) //polimorfismo
        {
            serie.setStart(100);
            for(int i = 0; i < 5; i++)
            {
                System.out.println(serie.getNext());
            }
            System.out.println("");
            serie.reset();
            for(int i = 0; i < 5; i++)
            {
                System.out.println(serie.getNext());
            }
            System.out.println("");
        }
    }
}
