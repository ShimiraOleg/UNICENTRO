public class Exercicio2 {
    public static void main(String[] args) {
        try {
            GeraExcecao.geraException();
        } catch (ArrayIndexOutOfBoundsException exc) {
            /* captura a exceção */
            System.out.println("\nMensagem padrão é: ");
            System.out.println(exc);
            System.out.println("\nRastreamento da pilha: ");
            exc.printStackTrace();
            /* obtem a informacao do stack trace */
            StackTraceElement[] traceElements = exc.getStackTrace();

            System.out.println("\nRastreamento da pilha obtido de exception.getStackTrace():");
            System.out.println("Classe\t\tArquivo\t\t\tLinha\tMetodo");

            /* itera pelos elementos para obter a descricao da excecao */
            for (StackTraceElement element : traceElements) {
                System.out.printf("%s\t", element.getClassName());
                System.out.printf("%s\t", element.getFileName());
                System.out.printf("%s\t", element.getLineNumber());
                System.out.printf("%s\n", element.getMethodName());
            }
        }

    }
}