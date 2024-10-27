package com.trabalhojava.sistemarpg.main;

import java.sql.SQLException;
import com.trabalhojava.sistemarpg.dao.PersonagemDAO;
import com.trabalhojava.sistemarpg.dao.PersonagemDBDAO;
import com.trabalhojava.sistemarpg.model.Personagem;
import com.trabalhojava.sistemarpg.dao.SistemaDAO;
import com.trabalhojava.sistemarpg.dao.SistemaDBDAO;
import com.trabalhojava.sistemarpg.model.Sistema;

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

        Sistema sistema1 = new Sistema(1,"Torment");
        Sistema sistema2 = new Sistema(2,"Call of Cthulhu");
        SistemaDBDAO sistemaDAO = new SistemaDBDAO();
        System.out.println("INSERE SISTEMAS");
        sistemaDAO.insere(sistema1);
        sistemaDAO.insere(sistema2);
        Sistema sistema3 = new Sistema(1,"Tormenta");
        System.out.println("ATUALIZA SISTEMA");
        sistemaDAO.atualizar(sistema3);
        System.out.println("LISTA SISTEMA");
        System.out.println(sistemaDAO.listar());
        System.out.println("REMOVE SISTEMA");
        sistemaDAO.remover(sistema2);
    }
}
