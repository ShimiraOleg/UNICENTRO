public class AppTrabalho {
    public static void main(String[] args) {
        Dispositivo d1 = new Dispositivo(1, "Notebook");
        Dispositivo d2 = new Dispositivo(2, "Desktop");

        Usuario u1 = new Usuario(1, "Theodoro");
        Usuario u2 = new Usuario(2, "Ana");

        u1.setDispositivo(d1);
        u1.trabalhar();
        u2.setDispositivo(d2);
        u2.trabalhar();
    }
}
