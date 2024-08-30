public class Inicia {
    public static void main(String[] args) {
        TiqueTaque tt = new TiqueTaque();
        MyThread mt1 = new MyThread("Tique", tt);
        MyThread mt2 = new MyThread("Taque", tt);
        try {
            mt1.thrd.join();
            mt2.thrd.join();
        } catch(InterruptedException exc) {
            System.out.println("Thread principal interrompida.");
        }
    }
}