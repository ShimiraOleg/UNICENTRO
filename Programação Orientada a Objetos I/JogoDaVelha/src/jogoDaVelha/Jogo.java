package jogoDaVelha;
import entradaDados.Console;

/**
 Código que rege as regras do jogo da velha
 @version 0.8
 @author Mateus de Oliveira Lopes
 */
public class Jogo extends Console{
    private char vencedor;
    private boolean isWin = false;
    private boolean j1Turno = true;
    private Tabuleiro tab = new Tabuleiro();

    /**
     * Função que ferifica se existe algum padrão vencedor no tabuleiro
     * @param tab o tabuleiro a ser verificado.
     * @return o simbolo do vencedor (empate envia 1).
     */
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

    /**
     * Função que analiza se existe um vencedor e para o jogo no caso de alguém vencer/empatar
     * @param qntRodadas a rodada atual
     * @param vencedor o simbolo a ser analizado
     * @param jVencedor o jogador da rodada atual
     * @return uma boolean que determina se o jogo paro ou continua
     */
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

    /**
     * Função que faz o loop de uma partida de jogo da velha
     * @param j1 o jogador 1
     * @param j2 o jogador 2
     * @param mJ o modo de jogo
     */
    public void jogando(Jogador j1, Jogador j2, int mJ)
    {
        Jogador jAtual;
        printTabuleiro(tab.getTabuleiro());
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
            j1Turno = Jogada.jogada(tab, jAtual, j1Turno,mJ);
            printTabuleiro(tab.getTabuleiro());
            vencedor = verificarSeTemVencedor(tab.getTabuleiro());
            isWin = analizarVencedor(tab.getRodadas(), vencedor, jAtual);
        }
    }

    /**
     * Função que reseta os jogadores e o tabuleiro para suas versões iniciais
     * @param j1
     * @param j2
     */
    public void reiniciar(Jogador j1, Jogador j2)
    {
       tab.setRodadas(0);
       j1.setTrocas(3);
       j2.setTrocas(3);
       tab = new Tabuleiro();
       isWin = false;
       j1Turno = true;
    }
}