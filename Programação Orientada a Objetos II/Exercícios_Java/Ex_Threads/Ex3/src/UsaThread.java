public class UsaThread {
    public static void main(String[] args) {
        System.out.println("Thread principal iniciando.");
        MyThread mt1 = new MyThread("Filha #1");
        MyThread mt2 = new MyThread("Filha #2");
        MyThread mt3 = new MyThread("Filha #3");

        Thread Thread1 = new Thread(mt1);
        Thread Thread2 = new Thread(mt2);
        Thread Thread3 = new Thread(mt3);
        Thread1.start();
        Thread2.start();
        Thread3.start();
        for (int i = 0; i < 50; i++) {
            System.out.print(".");
            try {
                Thread.sleep(100);
            } catch (InterruptedException exc) {
                System.out.println("Thread principal interrompida.");
            }
        }
        System.out.println("Thread principal finalizando.");
    }
}
