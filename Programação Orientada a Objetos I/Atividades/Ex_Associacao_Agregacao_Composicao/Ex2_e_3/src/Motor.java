public class Motor {
    private String tipo;

    public Motor(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString()
    {
        return tipo + " ";
    }
}
