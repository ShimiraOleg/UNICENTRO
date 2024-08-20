public class MaisTres implements Series{
    private int inicio;
    private int valor;

    MaisTres()
    {
        inicio = 0;
        valor = 0;
    }

    public void setStart(int x)
    {
        inicio = x;
        valor = inicio;
    }

    public void reset()
    {
        valor = inicio;
    }

    public int getNext()
    {
        valor += 3;
        return valor;
    }
}
