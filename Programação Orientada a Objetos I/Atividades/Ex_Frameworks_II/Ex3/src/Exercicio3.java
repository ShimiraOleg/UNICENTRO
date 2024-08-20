import java.util.*;
public class Exercicio3 {
    public static void main(String[] args) {
        String[] cores = { "preto", "amarelo", "verde", "azul", "branco" };
        List<String> list1 = new LinkedList<>(Arrays.asList(cores));
        System.out.println("\nImprimindo a Lista 1: ");
        printList(list1);
        String[] cores2 = {"dourado", "prata", "marron", "cinza"};
        List<String> list2 = new LinkedList<>(Arrays.asList(cores2));
        System.out.println("\nImprimindo a Lista 2: ");
        printList(list2);
        List<String> list3 = new LinkedList<>();
        list3.addAll(list1);
        list3.addAll(list2);
        System.out.println("\nImprimindo a Lista 3: ");
        printList(list3);
    }

    public static void printList(List<String> lista)
    {
        for(String l : lista)
        {
            System.out.println(l);
        }
    }
}