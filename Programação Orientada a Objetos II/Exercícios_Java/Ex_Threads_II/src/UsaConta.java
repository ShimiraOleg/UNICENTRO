public class UsaConta {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Pessoa #1");
        Pessoa p2 = new Pessoa("Pessoa #2");

        try{
            p1.thread.join();
            p2.thread.join();
        } catch (InterruptedException exc) {
            System.out.println("Thread Interrompida");
        }
    }
}
