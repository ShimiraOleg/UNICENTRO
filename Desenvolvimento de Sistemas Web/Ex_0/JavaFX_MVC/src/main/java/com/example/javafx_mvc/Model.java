package com.example.javafx_mvc;

public class Model {
    String frase, autor, autorCitacao, fraseCitacao;

    public Model() {
    }

    public void setFraseAutor(String aFrase, String aAutor) {
        this.frase = aFrase;
        this.autor = aAutor;
    }

    public void embelezarFrase() {
        fraseCitacao = "\"" + frase + "\"";
    }

    public void dividirAutor(){
        String[] autorDividido = autor.split(" ");
        autorCitacao = autorDividido[autorDividido.length-1] + ", " + autorDividido[0];
    }

    public String getAutorCitacao() {
        return autorCitacao;
    }

    public String getFraseCitacao() {
        return fraseCitacao;
    }
}