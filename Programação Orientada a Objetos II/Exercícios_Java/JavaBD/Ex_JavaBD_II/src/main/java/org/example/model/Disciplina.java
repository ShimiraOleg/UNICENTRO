package org.example.model;

public class Disciplina {
    private int disciplinaId;
    private String nome;

    public Disciplina()
    {

    }

    public Disciplina(int disciplinaId, String nome)
    {
        this.disciplinaId = disciplinaId;
        this.nome = nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setDisciplinaId(int disciplinaId) {
        this.disciplinaId = disciplinaId;
    }

    public String getNome() {
        return nome;
    }

    public int getDisciplinaId() {
        return disciplinaId;
    }

    @Override
    public String toString() {
        return "Disciplina{" +
                "disciplinaId=" + disciplinaId +
                ", nome='" + nome + '\'' +
                '}';
    }
}
