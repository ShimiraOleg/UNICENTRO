/*
Código que rege as regras do jogo da velha
@version 0.6
@author Mateus de Oliveira Lopes
 */
package jogoDaVelha;
import entradaDados.Console;

public class Jogo{
    private char vencedor;
    private boolean isWin = false;
    private boolean j1Turno = true;
    private Tabuleiro tab = new Tabuleiro();

    public char verificarSeTemVencedor(String[] tab)
    {
        for(int i = 0; i < 8; i++)
        {
            String v = null;
            switch (i){
                case 0:
                    v = tab[0] + tab[1] + tab[2];
                    break;
                case 1:
                    v = tab[3] + tab[4] + tab[5];
                    break;
                case 2:
                    v = tab[6] + tab[7] + tab[8];
                    break;
                case 3:
                    v = tab[0] + tab[3] + tab[6];
                    break;
                case 4:
                    v = tab[1] + tab[4] + tab[7];
                    break;
                case 5:
                    v = tab[2] + tab[5] + tab[8];
                    break;
                case 6:
                    v = tab[0] + tab[4] + tab[8];
                    break;
                case 7:
                    v = tab[6] + tab[4] + tab[2];
                    break;
            }
            if(v.equals("XXX"))
            {
                vencedor = 'X';
                break;
            }
            else if(v.equals("OOO"))
            {
                vencedor = 'O';
                break;
            }
            else
            {
                vencedor = '1';
            }

        }
        return vencedor;
    }

    public boolean analizarVencedor(int qntRodadas,char vencedor, Jogador jVencedor)
    {
        if(vencedor == 'X' || vencedor == 'O')
        {
            System.out.println("Jogador "+ jVencedor.getNome() +" (jogando com "+ jVencedor.getSimbolo() +") ganhou!");
            int p = jVencedor.getPontos();
            jVencedor.setPontos(p+1);
            return true;
        }
        else if (qntRodadas == 9 && vencedor == '1')
        {
            System.out.println("Empatou!");
            return true;
        }
        else {
            System.out.println("Jogo em Andamento");
            return false;
        }
    }

    public void jogando(Jogador j1, Jogador j2, Jogador jAtual)
    {
        int rodadas = 0;
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

            System.out.println("\nTurno do jogador: " + jAtual.getNome() + " (" + jAtual.getSimbolo() + ")");
            j1Turno = Jogada.jogada(tab, jAtual, j1Turno);
            Console.printTabuleiro(tab.getTabuleiro());
            vencedor = verificarSeTemVencedor(tab.getTabuleiro());
            isWin = analizarVencedor(rodadas, vencedor, jAtual);
        }
    }

    public void mostrarPontuacao(Jogador j1, Jogador j2)
    {
        System.out.println("\nPontuação de " + j1.getNome() + " (" + j1.getSimbolo() + "):\n" + j1.getPontos());
        System.out.println("Pontuação de " + j2.getNome() + " (" + j2.getSimbolo() + "):\n" + j2.getPontos());
    }

    public void reiniciar()
    {
       tab.setRodadas(0);
       tab = new Tabuleiro();
       isWin = false;
       j1Turno = true;
    }
}