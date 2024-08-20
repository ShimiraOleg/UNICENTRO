public class Microondas {
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
            System.out.println("Microondas Ligado");
        }
        else {
            System.out.println("Microondas Desligado");
        }
    }

    public boolean isLigado(boolean ligado)
    {
        return ligado;
    }
}
