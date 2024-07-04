package jogoDaVelha;

public class Main {
    public static void main(String[] args) {
        Tabuleiro tab = new Tabuleiro();
        tab.setTabuleiro("X", 0);
        tab.setTabuleiro("X", 1);
        tab.setTabuleiro("X", 2);
        tab.verificarVencedor(tab.getTabuleiro());
    }
}
