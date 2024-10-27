package com.trabalhojava.sistemarpg.dao;

import java.sql.SQLException;
import java.util.List;
import com.trabalhojava.sistemarpg.model.Sistema;

public interface SistemaDAO {
    void insere(Sistema var1) throws SQLException;
    void atualizar(Sistema var1) throws SQLException;
    void remover(Sistema var1) throws SQLException;
    List<Sistema> listar() throws SQLException;
}
