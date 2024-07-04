package jogoDaVelha;

public class Main {
    public static void main(String[] args) {
        char vencedor;
        Tabuleiro tab = new Tabuleiro();
        tab.setTabuleiro("O", 6);
        tab.setTabuleiro("O", 4);
        tab.setTabuleiro("O", 2);
        vencedor = tab.verificarVencedor(tab.getTabuleiro());
        System.out.println("Vencedor = " + vencedor);
    }

}
