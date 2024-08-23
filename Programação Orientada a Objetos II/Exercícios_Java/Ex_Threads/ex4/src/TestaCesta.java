public class TestaCesta {
    public static void main(String[] args) {
        CestaFrutas cf = new CestaFrutas();
        cf.AdcionarCestaFrutas("Maça");
        cf.AdcionarCestaFrutas("Banana");
        cf.AdcionarCestaFrutas("Abóbora");
        cf.AdcionarCestaFrutas("Maça");

        Thread td = new Thread(cf);
        td.start();
    }
}
