package org.example.dao;

import org.example.model.Disciplina;

import java.sql.SQLException;
import java.util.List;

public interface DisciplinaDAO {
    public void insere(Disciplina disciplina) throws SQLException;
    public void atualiza(Disciplina disciplina) throws SQLException;
    public void remove(Disciplina disciplina) throws SQLException;
    public Disciplina buscaPorCodigo(int DisciplinaId) throws SQLException;
    public List<Disciplina> listaTodos() throws SQLException;
}
