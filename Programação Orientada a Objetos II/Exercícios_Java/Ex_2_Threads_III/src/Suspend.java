public class Suspend {
    public static void main(String[] args) {
        MyThread ob1 = new MyThread("Minha Thread");
        try {
            Thread.sleep(1000);
            ob1.mySuspend();
            System.out.println("Suspendendo thread.");
            Thread.sleep(1000);

            ob1.myResume();
            System.out.println("Retomando thread.");
            Thread.sleep(1000);

            ob1.mySuspend();
            System.out.println("Suspendendo thread.");
            Thread.sleep(1000);

            ob1.myResume();
            System.out.println("Retomando thread.");
            Thread.sleep(1000);

            ob1.mySuspend();
            System.out.println("Encerrando thread.");
            ob1.myStop();
        } catch (InterruptedException e) {
            System.out.println("Thread principal interrompida");
        }
        // espera a thread terminar
        try {
            ob1.thrd.join();
        } catch (InterruptedException e) {
            System.out.println("Thread principal interrompida");
        }
        System.out.println("Thread principal encerrando.");
    }
}