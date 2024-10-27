package com.trabalhojava.sistemarpg.dao;

import com.trabalhojava.sistemarpg.model.Sistema;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class SistemaDBDAO implements SistemaDAO, IConst {
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;

    public SistemaDBDAO() {}

    public void open() throws SQLException {
        this.connection = Conexao.getConexao("jdbc:postgresql://localhost:5432/sistemarpg", "postgres", "postgres");
    }

    private void close() throws SQLException {
        this.connection.close();
    }

    public void insere(Sistema sistema) throws SQLException {
        this.open();
        this.sql = "INSERT INTO sistema(sistemaId,nome) VALUES (?, ?)";
        this.statement = this.connection.prepareStatement(this.sql);
        this.statement.setInt(1, sistema.getSistemaId());
        this.statement.setString(2, sistema.getNome());
        this.statement.executeUpdate();
        this.close();
    }

    public void atualizar(Sistema sistema) throws SQLException {
        this.open();
        this.sql = "UPDATE sistema SET nome=? WHERE sistemaId=?";
        this.statement = connection.prepareStatement(sql);
        this.statement.setString(1, sistema.getNome());
        this.statement.setInt(2, sistema.getSistemaId());
        this.statement.executeUpdate();
        this.close();
    }

    public void remover(Sistema sistema) throws SQLException {
        this.open();
        this.sql = "DELETE FROM sistema WHERE sistemaId=?";
        this.statement = this.connection.prepareStatement(this.sql);
        this.statement.setInt(1,sistema.getSistemaId());
        this.statement.executeUpdate();
        this.close();
    }

    public List<Sistema> listar() throws SQLException {
        this.open();
        this.sql = "SELECT * FROM sistema";
        this.statement = this.connection.prepareStatement(this.sql);
        this.result = this.statement.executeQuery();
        ArrayList<Sistema> sistemas = new ArrayList<>();

        while (this.result.next()) {
            Sistema sistema = new Sistema();
            sistema.setSistemaId(this.result.getInt("sistemaId"));
            sistema.setNome(this.result.getString("nome"));
            sistemas.add(sistema);
        }
        this.close();
        return sistemas;
    }
}
