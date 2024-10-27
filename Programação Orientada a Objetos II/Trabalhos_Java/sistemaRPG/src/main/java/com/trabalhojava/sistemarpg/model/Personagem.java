package com.trabalhojava.sistemarpg.model;

public class Personagem {
    private int personagemId;
    private String nome;
    private String descricao;
    private String urlImg;
    private int nivel;
    private int forca;
    private int destreza;
    private int constituicao;
    private int inteligencia;
    private int sabedoria;
    private int carisma;

    public Personagem() {}

    public Personagem(int personagemId, String nome, String descricao, String urlImg, int nivel, int forca, int destreza,
                      int constituicao, int inteligencia, int sabedoria, int carisma) {
        this.personagemId = personagemId;
        this.nome = nome;
        this.descricao = descricao;
        this.urlImg = urlImg;
        this.nivel = nivel;
        this.forca = forca;
        this.destreza = destreza;
        this.constituicao = constituicao;
        this.inteligencia = inteligencia;
        this.sabedoria = sabedoria;
        this.carisma = carisma;
    }

    public int getPersonagemId() {
        return personagemId;
    }

    public String getNome() {
        return nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public String getUrlImg() {
        return urlImg;
    }

    public int getNivel() {
        return nivel;
    }

    public int getForca() {
        return forca;
    }

    public int getDestreza() {
        return destreza;
    }

    public int getConstituicao() {
        return constituicao;
    }

    public int getInteligencia() {
        return inteligencia;
    }

    public int getSabedoria() {
        return sabedoria;
    }

    public int getCarisma() {
        return carisma;
    }

    public void setPersonagemId(int personagemId) {
        this.personagemId = personagemId;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public void setUrlImg(String urlImg) {
        this.urlImg = urlImg;
    }

    public void setNivel(int nivel) {
        this.nivel = nivel;
    }

    public void setForca(int forca) {
        this.forca = forca;
    }

    public void setDestreza(int destreza) {
        this.destreza = destreza;
    }

    public void setConstituicao(int constituicao) {
        this.constituicao = constituicao;
    }

    public void setInteligencia(int inteligencia) {
        this.inteligencia = inteligencia;
    }

    public void setSabedoria(int sabedoria) {
        this.sabedoria = sabedoria;
    }

    public void setCarisma(int carisma) {
        this.carisma = carisma;
    }

    public String toString(){
        return "Personagem {personagemId=" + this.personagemId +
                ", nome=" + this.nome +
                ", descricao=" + this.descricao +
                ", urlImg=" + this.urlImg +
                ", nivel=" + this.nivel +
                ", força=" + this.forca +
                ", destreza=" + this.destreza +
                ", constituição=" + this.constituicao +
                ", inteligência" + this.inteligencia +
                ", sabedoria" + this.sabedoria +
                ", carisma" + this.carisma + "}";
    }
}
