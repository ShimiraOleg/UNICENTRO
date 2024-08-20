public class TesteDoisGen {
    public static void main(String[] args) {
        DoisGen<Integer, String> objDuplo;
        objDuplo = new DoisGen<Integer, String>(42, "Teste");

        objDuplo.showType();

        System.out.println("Valor ob1: " + objDuplo.getOb1());
        System.out.println("Valor ob2: " + objDuplo.getOb2());
    }
}
