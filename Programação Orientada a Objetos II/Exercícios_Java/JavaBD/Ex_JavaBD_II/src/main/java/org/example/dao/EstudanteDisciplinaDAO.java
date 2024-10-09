package org.example.dao;

import org.example.model.Estudante;
import org.example.model.EstudanteDisciplina;

import java.sql.SQLException;
import java.util.List;

public interface EstudanteDisciplinaDAO {
    public void insere(EstudanteDisciplina estudanteDisciplina) throws SQLException;
    public void atualiza(EstudanteDisciplina estudanteDisciplinaNovo, EstudanteDisciplina estudanteDisciplinaVelho) throws SQLException;
    public void remove(EstudanteDisciplina estudanteDisciplina) throws SQLException;
    public EstudanteDisciplina buscaIndividual(int estudanteId, int disciplinaId) throws SQLException;
    public List<EstudanteDisciplina> listaTodos() throws SQLException;
}
