import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

import static java.util.Collections.*;

public class TesteFuncaoList {
    public static void main(String[] args) {
        List<String> nomes = new ArrayList<>();
        nomes.add("Renan");
        nomes.add("Luigi");
        nomes.add("Mario");
        nomes.add("Lucas");
        nomes.add("Paulo");
        System.out.println("original: ");
        imprimir(nomes);
        sort(nomes); //Ordena a lista de maneira crescente, seguindo a ordem natural de seus elementos
        System.out.println("\nsort: ");
        imprimir(nomes);
        binarySearch(nomes, "Renan"); /*Verifica se a lista contém o elemento requisitado (ela deve
                                             estar na ordem crescente seguindo a ordem natural de seus elementos para funcionar)*/
        System.out.println("\nbinarySearch: ");
        imprimir(nomes);
        reverse(nomes); //Inverte a ordem dos elementos da lista
        System.out.println("\nreverse: ");
        imprimir(nomes);
        replaceAll(nomes,"Renan","André"); /*Troca todos os elementos da lista com o mesmo valor inserido
                                                         pelo novo valor inserido*/
        System.out.println("\nreplaceAll: ");
        imprimir(nomes);
        rotate(nomes,2); //Rotaciona os elementos da lista pela distancia inserida
        System.out.println("\nrotate: ");
        imprimir(nomes);
    }
    public static void imprimir(List<String> nome)
    {
        for(String n:nome)
        {
            System.out.println("Nome: " + n);
        }
    }
}
