public class GeraExcecao {
    static void geraException() {
        int[] nums = new int[4];
        System.out.println("Antes da exceção ser gerada.");
        /* gera uma exceção do tipo índice do array está fora dos limites */
        nums[7] = 10;
        System.out.println("Isto não será exibido!");
    }
}