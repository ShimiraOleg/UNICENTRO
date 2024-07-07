package jogoDaVelha;

import entradaDados.Console;

import java.lang.invoke.ConstantCallSite;

public class Main {
    public static void main(String[] args) {
        char vencedor;
        Console con = new Console();
        boolean isWin = false;
        Tabuleiro tab = new Tabuleiro();
        while(tab.getRodadas() < 9 && !(isWin))
        {
            con.printTabuleiro(tab.getTabuleiro());
            tab.setTabuleiro("O", con.receberEntradaJogada());
            vencedor = tab.verificarSeTemVencedor(tab.getTabuleiro());
            isWin = tab.analizarVencedor(tab.getRodadas(), vencedor);
            tab.setRodadas();
        }
    }

}
