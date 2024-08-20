import java.util.ArrayList;

public class UsaContaBanco {
    public static void main(String[] args) {
        ArrayList<ContaBanco> contas = new ArrayList<ContaBanco>();
        contas.add(new ContaBanco(45, 5000.19 ));
        contas.add(new ContaBanco(42));
        contas.add(new ContaBanco(125, 100.75));

        System.out.println("Total de instancias de contas: " + contas.size() + "\n");
        testaBanco(contas, true);
        contas.removeFirst();
        System.out.println("Total de instancias de contas: " + contas.size() + "\n");
        testaBanco(contas, false);
        System.out.println("Primeira instância: " + contas.getFirst());
        System.out.println("Ultima instância: " + contas.getLast());

    }

    public static void testaBanco(ArrayList<ContaBanco> c, boolean fazSaqueEDeposito)
    {
        if(fazSaqueEDeposito)
        {
            for(int i = 0; i < c.size(); i++)
            {
                System.out.println(c.get(i));
                c.get(i).deposito(100.81);
                System.out.println(c.get(i));
                c.get(i).saque(50.81);
                System.out.println(c.get(i) +  "\n");
            }
        }
        else {
            for(int i = 0; i < c.size(); i++)
            {
                System.out.println(c.get(i));
            }
            System.out.println();
        }
    }
}
