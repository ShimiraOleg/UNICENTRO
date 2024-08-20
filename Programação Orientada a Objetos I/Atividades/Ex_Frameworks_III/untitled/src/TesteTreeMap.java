import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class TesteTreeMap {
    public static void main(String[] args) {
        TreeMap<String, Integer> alunos = new TreeMap<String, Integer>();

        alunos.put("Gilmar Bolivar",9);
        alunos.put("Rodrigo Palhano Almeida",2);
        alunos.put("André Fernando Tozzi",6);
        alunos.put("João Paulo Antunes Gomes",9);
        alunos.put("Vitor Pinto Junior",7);

        Set<Map.Entry<String, Integer>> alunoNotas = alunos.entrySet();

        System.out.println("Listagem 1 de Alunos:");
        for(Map.Entry<String,Integer> aN : alunoNotas)
        {
            System.out.println("Aluno: " + aN.getKey() + " - Nota: " + aN.getValue());
        }

        alunos.put("André Fernando Tozzi", 9);

        System.out.println("\nListagem 2 de Alunos:");
        for(Map.Entry<String,Integer> aN : alunoNotas)
        {
            System.out.println("Aluno: " + aN.getKey() + " - Nota: " + aN.getValue());
        }
    }
}
