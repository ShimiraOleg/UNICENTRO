public class Carro {
    private String marca;
    private String modelo;
    private String fabricante;
    private Motor motor;
    private Bancos banco;

    public Carro(String marca, String modelo, String fabricante, Motor motor, Bancos banco) {
        this.marca = marca;
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.motor = motor;
        this.banco = banco;
    }

    @Override
    public String toString()
    {
        return fabricante + " " + marca + " " + modelo + " " + motor + banco;
    }
}
