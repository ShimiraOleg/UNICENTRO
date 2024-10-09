package org.example.model;

public class Estudante {
    private int estudanteId;
    private String nome;
    private int idade;

    public Estudante()
    {

    }

    public Estudante(int estudanteId, String nome, int idade)
    {
        this.estudanteId = estudanteId;
        this.nome = nome;
        this.idade = idade;
    }

    public void setEstudanteId(int estudanteId) {
        this.estudanteId = estudanteId;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getEstudanteId() {
        return estudanteId;
    }

    public int getIdade() {
        return idade;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Estudante{" +
                "estudanteId=" + estudanteId +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                '}';
    }
}
