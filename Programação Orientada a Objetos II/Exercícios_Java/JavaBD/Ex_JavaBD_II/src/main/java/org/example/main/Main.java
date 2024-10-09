package org.example.main;

import java.sql.SQLException;

import org.example.dao.DisciplinaDBDAO;
import org.example.dao.EstudanteDBDAO;
import org.example.dao.EstudanteDisciplinaDBDAO;
import org.example.model.Disciplina;
import org.example.model.Estudante;
import org.example.model.EstudanteDisciplina;

public class Main {

    public static void main(String[] args) throws SQLException {
        Estudante estudante = new Estudante(1, "André", 22);
        EstudanteDBDAO estudanteDAO = new EstudanteDBDAO();

        System.out.println("######### Operações sobre a tabela Estudante ###########");

        System.out.println("Insere o estudante André:");
        estudanteDAO.insere(estudante);

        System.out.println("Lista os estudantes no banco:");
        //Chamadas a println com apenas um objeto fazem com que toString seja chamado
        //automaticamente.
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Muda o nome de André para André Galvão e idade de 22 para 17:");
        Estudante estudante01 = new Estudante(1, "André Galvão", 17);
        estudanteDAO.atualiza(estudante01);

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Insere o estudante Mario:");
        Estudante estudante02 = new Estudante(2, "Mario", 23);
        estudanteDAO.insere(estudante02);

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Insere a estudante Mariane:");
        Estudante estudante03 = new Estudante(3, "Mariane", 19);
        estudanteDAO.insere(estudante03);

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("Retorna o estudante Mario:");
        System.out.println(estudanteDAO.buscaPorCodigo(2));

        System.out.println("Remove o estudante Mario:");
        estudanteDAO.remove(estudanteDAO.buscaPorCodigo(2));

        System.out.println("Lista os estudantes no banco:");
        System.out.println(estudanteDAO.listaTodos());

        System.out.println("\n######### Operações sobre a tabela Disciplina ###########");

        Disciplina disciplina = new Disciplina(1, "Matemática");
        DisciplinaDBDAO disciplinaDAO = new DisciplinaDBDAO();

        System.out.println("Insere a disciplina Matemática:");
        disciplinaDAO.insere(disciplina);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Muda o nome de Matemática para Cálculo I:");
        Disciplina disciplina01 = new Disciplina(1, "Cálculo I");
        disciplinaDAO.atualiza(disciplina01);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Insere a disciplina Português:");
        Disciplina disciplina02 = new Disciplina(2, "Português");
        disciplinaDAO.insere(disciplina02);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Insere a disciplina Inglés:");
        Disciplina disciplina03 = new Disciplina(3, "Inglés");
        disciplinaDAO.insere(disciplina03);

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("Retorna a disciplina Português:");
        System.out.println(disciplinaDAO.buscaPorCodigo(2));

        System.out.println("Remove a disciplina Português:");
        disciplinaDAO.remove(disciplinaDAO.buscaPorCodigo(2));

        System.out.println("Lista as disciplinas no banco:");
        System.out.println(disciplinaDAO.listaTodos());

        System.out.println("\n######### Operações sobre a tabela EstudanteDisciplina ###########");

        EstudanteDisciplina estudanteDisciplina = new EstudanteDisciplina();
        estudanteDisciplina.setEstudante(estudanteDAO.buscaPorCodigo(1));
        estudanteDisciplina.setDisciplina(disciplinaDAO.buscaPorCodigo(1));

        System.out.println("Cria relação entre estudante e disciplina:");
        EstudanteDisciplinaDBDAO estudanteDisciplinaDAO = new EstudanteDisciplinaDBDAO();
        estudanteDisciplinaDAO.insere(estudanteDisciplina);

        System.out.println("Lista todas as relações entre estudante e disciplina:");
        System.out.println(estudanteDisciplinaDAO.listaTodos());
    }
}
