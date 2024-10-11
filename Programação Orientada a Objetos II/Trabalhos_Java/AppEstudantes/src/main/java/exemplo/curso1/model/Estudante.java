package exemplo.curso1.model;

public class Estudante {
    private int estudanteID;
    private String nome;
    private int idade;

    public Estudante() {

    }
    public Estudante(int estudanteID, String nome, int idade) {
        this.estudanteID = estudanteID;
        this.nome = nome;
        this.idade = idade;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public Estudante(int idade) {
        this.idade = idade;
    }

    public int getEstudanteID() {
        return estudanteID;
    }

    public void setEstudanteID(int estudanteID) {
        this.estudanteID = estudanteID;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Estudante{" +
                "estudanteID=" + estudanteID +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                '}';
    }
}