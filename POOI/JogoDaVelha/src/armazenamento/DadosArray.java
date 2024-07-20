/*
Classe para criar um objeto que guarda um Int e um String para serem usados em um ArrayList.
@version 1.0
@author Yan Gabriel Reis Oliveira
*/
package armazenamento;

public class DadosArray {
    private String nome;
    private int pontuacao;
    
    /*
     * Construtor da classe DadosArray.
     */
    public DadosArray(String nome, int pontuacao){
        this.nome = nome;
        this.pontuacao = pontuacao;
    }
    
    /*
     * Método para retornar o nome do jogador.
     */
    public String getNome(){
        return nome;
    }
    
    /*
     * Método para retornar a pontuação do jogador.
     */
    public int getPontuacao(){
        return pontuacao;
    }
    
    /*
     * Método para definir o nome do jogador.
     */
    public void setNome(String nome){
        this.nome = nome;
    }
    
    /*
     * Método para definir a pontuação do jogador.
     */
    public void setPontuacao(int pontuacao){
        this.pontuacao = pontuacao;
    }

    /*
     * Atualizacao do metodo toString para retornar o nome e a pontuacao do jogador.
     */
    @Override
    public String toString() {
        return (
                "Jogador: " + nome + '\'' +
                ", Pontos: " + pontuacao + '\'' )
              ;
    }
}