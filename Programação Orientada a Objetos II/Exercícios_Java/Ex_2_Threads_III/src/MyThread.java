public class MyThread implements Runnable {
    Thread thrd;
    boolean suspender;
    boolean encerrar;
    MyThread(String name) {
        thrd = new Thread(this, name);
        suspender = false;
        encerrar = false;
        thrd.start();
    }

    // Este � o ponto de entrada para a Thread.
    public void run() {
        System.out.println(thrd.getName() + " iniciando.");
        try {
            for (int i = 1; i < 1000; i++) {
                System.out.print(i + " ");
                if ((i % 10) == 0) {
                    System.out.println();
                    Thread.sleep(250);
                }
                // Usa um bloco sincronizado para verificar suspender e encerrar.
                synchronized (this) {
                    while (suspender) {
                        wait();
                    }
                    if (encerrar)
                        break;
                }
            }
        } catch (InterruptedException exc) {
            System.out.println(thrd.getName() + " interrompido.");
        }
        System.out.println(thrd.getName() + " finalizando.");
    }
    // Finalizar uma thread.
    synchronized void myStop() {
        suspender = false;
        encerrar = true;
        notify();
    }
    // Suspender a thread.
    synchronized void mySuspend() {
        suspender = true;
        notify();
    }
    // Retomar a thread.
    synchronized void myResume() {
        suspender = false;
        notify();
    }
}