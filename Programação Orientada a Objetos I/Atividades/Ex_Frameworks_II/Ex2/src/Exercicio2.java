import java.util.*;
public class Exercicio2
{
    public static void main(String[] args)
    {
        String[] cores = {"vermelho", "branco", "azul", "verde", "cinza",
                "laranja", "laranja", "cinza","vermelho"};

        List <String> list = new ArrayList<>(Arrays.asList(cores));
        HashSet <String> list1 = new HashSet<String>();
        TreeSet <String> list2 = new TreeSet<String>();
        for(String l: list)
            list1.add(l);
        for (String l: list)
            list2.add(l);
        System.out.println("Array: ");
        printCollection(list);
        System.out.println("HashSet: ");
        printCollection(list1);
        System.out.println("TreeSet: ");
        printCollection(list1);
    }
    public static void printCollection(Collection<String> l)
    {
        System.out.println(l);
    }
}

