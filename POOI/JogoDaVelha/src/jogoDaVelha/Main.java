package jogoDaVelha;

public class Main {
    public static void main(String[] args) {
        char vencedor;
        boolean isWin = false;
        Tabuleiro tab = new Tabuleiro();

        while(tab.getRodadas() < 9 && !(isWin))
        {
            tab.setTabuleiro("O", 1);
            vencedor = tab.verificarSeTemVencedor(tab.getTabuleiro());
            isWin = tab.analizarVencedor(tab.getRodadas(), vencedor);
            tab.setRodadas();
        }
    }

}
