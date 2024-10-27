package com.trabalhojava.sistemarpg.model;

public class Sistema {
    private int sistemaId;
    private String nome;

    public Sistema() {}

    public Sistema(int sistemaId, String nome) {
        this.sistemaId = sistemaId;
        this.nome = nome;
    }

    public int getSistemaId() {
        return sistemaId;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setSistemaId(int sistemaId) {
        this.sistemaId = sistemaId;
    }

    public String toString() {
        return "Sistema { Sistema Id: " + this.sistemaId +
                ", Nome: " + this.nome + "}";
    }
}
