public class Pessoa implements Runnable{
    Thread thread;
    private ContaBancaria cb = new ContaBancaria();

    public Pessoa(String name)
    {
        thread = new Thread(this, name);
        thread.start();
    }

    @Override
    public void run()
    {
        System.out.println(thread.getName() + " Iniciada.\n");
        for(int i = 0; i < 10; i++)
        {
            try{
                synchronized (cb) {
                    cb.depositar();
                    System.out.println("Saldo de "+ thread.getName() + " após deposito: " + cb.getSaldo());
                }
                Thread.sleep(200);
                synchronized (cb) {
                    cb.sacar();
                    System.out.println("Saldo de "+ thread.getName() + " após saque: " + cb.getSaldo());
                }
                Thread.sleep(200);
            } catch (InterruptedException exc) {
                System.out.println("Thread Interrompida");
            }
        }
        System.out.println(thread.getName() + " Finalizada. Saldo Final: " + cb.getSaldo());
    }
}
