package com.trabalhojava.sistemarpg.dao;

import java.sql.SQLException;
import java.util.List;
import com.trabalhojava.sistemarpg.model.Personagem;

public interface PersonagemDAO {
    void insere(Personagem var1) throws SQLException;
    void atualizar(Personagem var1) throws SQLException;
    void remover(Personagem var1) throws SQLException;
    List<Personagem> listar() throws SQLException;
}
