public class MaisDois implements Series{
    private int inicio;
    private int valor;

    MaisDois()
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
        valor += 2;
        return valor;
    }
}