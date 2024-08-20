public class Geladeira {
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
            System.out.println("Geladeira Ligada");
        }
        else {
            System.out.println("Geladeira Desligada");
        }
    }

    public boolean isLigado(boolean ligado)
    {
        return ligado;
    }
}
