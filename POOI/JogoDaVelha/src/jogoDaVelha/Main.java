package jogoDaVelha;

import entradaDados.Console;

import java.lang.invoke.ConstantCallSite;

public class Main {
    public static void main(String[] args) {
        char vencedor;
        Jogador j1 = new Jogador("X", "Teste");
        Jogador j2 = new Jogador("O", "Testador");
        Jogador jAtual = new Jogador();
        boolean isWin = false;
        boolean j1Turno = true;
        Tabuleiro tab = new Tabuleiro();

        Console.printTabuleiro(tab.getTabuleiro());
        while(!(isWin))
        {
            if(j1Turno) {
                jAtual = j1;
                j1Turno = false;
            }
            else
            {
                jAtual = j2;
                j1Turno = true;
            }

            System.out.println("\nTurno do jogador: " + jAtual.nome + " (" + jAtual.getSimbolo() + ")");
            j1Turno = Jogada.jogada(tab, jAtual, j1Turno);
            Console.printTabuleiro(tab.getTabuleiro());
            vencedor = tab.verificarSeTemVencedor(tab.getTabuleiro());
            isWin = tab.analizarVencedor(tab.getRodadas(), vencedor, jAtual.nome);
        }
    }
    
}
