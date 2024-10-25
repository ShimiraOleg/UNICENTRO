package com.trabalhojava.sistemarpg.main;

import java.sql.SQLException;
import com.trabalhojava.sistemarpg.dao.PersonagemDAO;
import com.trabalhojava.sistemarpg.dao.PersonagemDBDAO;
import com.trabalhojava.sistemarpg.model.Personagem;

public class Main {
    public static void main(String[] args) throws SQLException{
        Personagem personagem = new Personagem(1,"Singus","The GOAT","Imagem Foda",17,-1,3,4,7,2,-2);
        Personagem personagem1 = new Personagem(2,"Degnis","The B","Imagem",12,-1,3,4,7,2,-2);
        PersonagemDBDAO personagemDAO = new PersonagemDBDAO();
        System.out.println("INSERE PERSONAGENS");
        personagemDAO.insere(personagem);
        personagemDAO.insere(personagem1);
        Personagem personagem2 = new Personagem(1,"Singed","GOAT","Imagem 2",18,-1,3,4,7,2,-2);
        System.out.println("ATUALIZA PERSONAGEM");
        personagemDAO.atualizar(personagem2);
        System.out.println("LISTA PERSONAGEM");
        System.out.println(personagemDAO.listar());
        System.out.println("REMOVE PERSONAGEM");
        personagemDAO.remover(personagem1);
    }
}
