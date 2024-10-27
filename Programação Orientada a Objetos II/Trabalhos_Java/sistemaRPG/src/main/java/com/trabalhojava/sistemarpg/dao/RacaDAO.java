package com.trabalhojava.sistemarpg.dao;

import java.sql.SQLException;
import java.util.List;
import com.trabalhojava.sistemarpg.model.Raca;

public interface RacaDAO {
    void insere(Raca var1) throws SQLException;
    void atualizar(Raca var1) throws SQLException;
    void remover(Raca var1) throws SQLException;
    List<Raca> listar() throws SQLException;
}
