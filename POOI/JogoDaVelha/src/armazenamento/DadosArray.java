package armazenamento;

public class DadosArray {
    private String nome;
    private int pontuacao;
    
    public DadosArray(String nome, int pontuacao){
        this.nome = nome;
        this.pontuacao = pontuacao;
    }
    
    public String getNome(){
        return nome;
    }
    
    public int getPontuacao(){
        return pontuacao;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public void setPontuacao(int pontuacao){
        this.pontuacao = pontuacao;
    }

    @Override
    public String toString() {
        return (
                "Jogador: " + nome + '\'' +
                ", Pontos: " + pontuacao + '\'' )
              ;
    }
}