import java.util.*;
public class ExemploTreeSet {
    public static void main(String[] args) {
        char[] chrs = { 'V', 'J', 'L', 'E', 'E' };
        // Cria um conjunto de àrvore e um conjunto hash.
        TreeSet<Character> ts = new TreeSet<Character>();
        HashSet<Character> hs = new HashSet<Character>();
        System.out.print("Conteúdo de chrs:      ");
        for(char ch : chrs)
            System.out.print(ch + "  ");
        System.out.println();
        // Primeiro, adiciona os caracteres ao conjunto hash.
        for(char ch : chrs)
            hs.add(ch);
        System.out.println("Conteúdo do conjunto hash: " + hs);
        // Em seguida, adiciona os caracteres ao conjunto da àrvore.
        for(char ch : chrs)
            ts.add(ch);
        System.out.println("Conteúdo do conjunto de àrvore: " + ts);
    }
}
