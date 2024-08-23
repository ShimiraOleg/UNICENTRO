import java.util.ArrayList;

public class CestaFrutas implements Runnable{
    private ArrayList<String> frutas = new ArrayList<String>();
    public void AdcionarCestaFrutas(String nomeFruta)
    {
        frutas.add(nomeFruta);
    }

    public void run() {
        System.out.println("Thread Inicializada");
        try {
            for(String i : frutas)
            {
                Thread.sleep(400);
                System.out.println(i);
            }
        } catch (InterruptedException exc) {
            System.out.println("Erro na Thread");
        }
        System.out.println("Thread Finalizada");
    }
}
