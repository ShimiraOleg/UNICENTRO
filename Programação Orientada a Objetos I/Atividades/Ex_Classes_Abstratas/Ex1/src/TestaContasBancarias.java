public class TestaContasBancarias {
    public static void main(String[] args) {
        ContaSimples cs1 = new ContaSimples("Howard");
        ContaEspecial ce1 = new ContaEspecial("Mauricio", 5000.0);

        cs1.deposita(4500.25);
        ce1.deposita(4100);

        cs1.retira(100);
        ce1.retira(100);
        cs1.retira(9000);
        ce1.retira(9000);
        ce1.retira(9000.01);
    }
}
