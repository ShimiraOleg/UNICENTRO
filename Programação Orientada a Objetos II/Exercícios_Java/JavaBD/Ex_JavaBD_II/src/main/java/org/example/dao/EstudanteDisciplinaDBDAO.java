package org.example.dao;

import org.example.model.EstudanteDisciplina;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class EstudanteDisciplinaDBDAO implements EstudanteDisciplinaDAO, IConst{
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;

    private void open() throws SQLException {
        connection = Conexao.getConexao(Conexao.stringDeConexao, Conexao.usuario, Conexao.senha);
    }

    private void close() throws SQLException {
        connection.close();
    }

    public void insere(EstudanteDisciplina estudanteDisciplina) throws SQLException{
        open();
        sql="INSERT INTO estudantedisciplina(estudante_id,disciplina_id) VALUES(?,?)";
        statement = connection.prepareStatement(sql);
        statement.setInt(1,estudanteDisciplina.getEstudante().getEstudanteId());
        statement.setInt(2,estudanteDisciplina.getDisciplina().getDisciplinaId());
        statement.executeUpdate();
        close();
    }

    public void atualiza(EstudanteDisciplina estudanteDisciplinaNovo, EstudanteDisciplina estudanteDisciplinaVelho) throws SQLException{
        open();
        sql="UPDATE estudantedisciplina SET estudante_id = ?, disciplina_id = ? WHERE estudante_id = ? AND disciplina_id = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1,estudanteDisciplinaNovo.getEstudante().getEstudanteId());
        statement.setInt(2,estudanteDisciplinaNovo.getDisciplina().getDisciplinaId());
        statement.setInt(3,estudanteDisciplinaVelho.getEstudante().getEstudanteId());
        statement.setInt(4,estudanteDisciplinaVelho.getDisciplina().getDisciplinaId());
        close();
    }

    public void remove(EstudanteDisciplina estudanteDisciplina) throws SQLException{
        open();
        sql="DELETE FROM estudantedisciplina WHERE estudante_id = ? AND disciplina_ID = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1, estudanteDisciplina.getEstudante().getEstudanteId());
        statement.setInt(2, estudanteDisciplina.getDisciplina().getDisciplinaId());
        close();
    }

    public EstudanteDisciplina buscaIndividual(int estudanteId, int disciplinaId) throws SQLException{
        open();
        sql = "SELECT * FROM estudantedisciplina WHERE estudante_id = ? AND disciplina_id = ?";
        statement = connection.prepareStatement(sql);
        statement.setInt(1,estudanteId);
        statement.setInt(2,disciplinaId);
        result = statement.executeQuery();
        EstudanteDBDAO estudanteDB = new EstudanteDBDAO();
        DisciplinaDBDAO disciplinaDB = new DisciplinaDBDAO();
        if(result.next()){
            EstudanteDisciplina estudanteDisciplina = new EstudanteDisciplina();
            estudanteDisciplina.setEstudante(estudanteDB.buscaPorCodigo(result.getInt("estudante_ID")));
            estudanteDisciplina.setDisciplina(disciplinaDB.buscaPorCodigo(result.getInt("disciplina_ID")));
            close();
            return estudanteDisciplina;
        } else {
            close();
            return null;
        }
    }

    public List<EstudanteDisciplina> listaTodos() throws SQLException{
        open();
        sql = "SELECT * FROM estudantedisciplina";
        statement = connection.prepareStatement(sql);
        result = statement.executeQuery();
        ArrayList<EstudanteDisciplina> estudantesDisciplinas = new ArrayList<>();
        EstudanteDBDAO estudanteDB = new EstudanteDBDAO();
        DisciplinaDBDAO disciplinaDB = new DisciplinaDBDAO();
        while (result.next())
        {
            EstudanteDisciplina estudanteDisciplina = new EstudanteDisciplina();
            estudanteDisciplina.setEstudante(estudanteDB.buscaPorCodigo(result.getInt("estudante_ID")));
            estudanteDisciplina.setDisciplina(disciplinaDB.buscaPorCodigo(result.getInt("disciplina_ID")));
            estudantesDisciplinas.add(estudanteDisciplina);
        }
        close();
        return estudantesDisciplinas;
    }
}
