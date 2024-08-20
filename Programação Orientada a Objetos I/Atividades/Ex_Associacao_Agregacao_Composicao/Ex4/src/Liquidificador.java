public class Liquidificador {
    private boolean ligado = false;

    public void ligar()
    {
        ligado = true;
    }

    public void desligar()
    {
        ligado = false;
    }

    public void observar()
    {
        if(isLigado(ligado))
        {
            System.out.println("Liquidificador Ligado");
        }
        else {
            System.out.println("Liquidificador Desligado");
        }
    }

    public boolean isLigado(boolean ligado)
    {
        return ligado;
    }
}
