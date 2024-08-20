public class Bancos {
    private String fabricante;

    public Bancos(String fabricante) {
        this.fabricante = fabricante;
    }

    @Override
    public String toString()
    {
        return fabricante + " ";
    }
}
