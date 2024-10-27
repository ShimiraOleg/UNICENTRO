package com.trabalhojava.sistemarpg.dao;

import com.trabalhojava.sistemarpg.model.Raca;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class RacaDBDAO implements RacaDAO, IConst {
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;

    public RacaDBDAO() {}

    private void open() throws SQLException {
        this.connection = Conexao.getConexao("jdbc:postgresql://localhost:5432/sistemarpg", "postgres", "postgres");
    }

    private void close() throws SQLException {
        this.connection.close();
    }

    public void insere(Raca raca) throws SQLException {
        this.open();
        this.sql = "INSERT INTO raca(racaId, nomeRaca, descricao, forca, destreza, constituicao, inteligencia, sabedoria, carisma, sistemaId) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
        this.statement = this.connection.prepareStatement(this.sql);
        this.statement.setInt(1, raca.getRacaId());
        this.statement.setString(2, raca.getNomeRaca());
        this.statement.setString(3, raca.getDescricao());
        this.statement.setInt(4, raca.getForca());
        this.statement.setInt(5, raca.getDestreza());
        this.statement.setInt(6, raca.getConstituicao());
        this.statement.setInt(7, raca.getInteligencia());
        this.statement.setInt(8, raca.getSabedoria());
        this.statement.setInt(9, raca.getCarisma());
        this.statement.setInt(10, raca.getSistemaId());
        this.statement.executeUpdate();
        this.close();
    }

    public void atualizar(Raca raca) throws SQLException {
        this.open();
        this.sql = "UPDATE raca SET nomeRaca=?, descricao=?, forca=?, destreza=?, constituicao=?, inteligencia=?, sabedoria=?, carisma=?, sistemaId=? WHERE racaId=?";
        this.statement = this.connection.prepareStatement(sql);
        this.statement.setString(1, raca.getNomeRaca());
        this.statement.setString(2, raca.getDescricao());
        this.statement.setInt(3, raca.getForca());
        this.statement.setInt(4, raca.getDestreza());
        this.statement.setInt(5, raca.getConstituicao());
        this.statement.setInt(6, raca.getInteligencia());
        this.statement.setInt(7, raca.getSabedoria());
        this.statement.setInt(8, raca.getCarisma());
        this.statement.setInt(9, raca.getSistemaId());
        this.statement.setInt(10, raca.getRacaId());
        this.statement.executeUpdate();
        this.close();
    }

    public void remover(Raca raca) throws SQLException {
        this.open();
        this.sql = "DELETE FROM raca WHERE id=?";
        this.statement = connection.prepareStatement(sql);
        this.statement.setInt(1,raca.getRacaId());
        this.statement.executeUpdate();
        this.close();
    }

    public List<Raca> listar() throws SQLException {
        this.open();
        this.sql = "SELECT * FROM raca";
        this.statement = this.connection.prepareStatement(this.sql);
        this.result = this.statement.executeQuery();
        ArrayList<Raca> racas = new ArrayList<>();

        while (this.result.next()) {
            Raca raca = new Raca();
            raca.setRacaId(this.result.getInt("racaId"));
            raca.setNomeRaca(this.result.getString("nomeRaca"));
            raca.setDescricao(this.result.getString("descricao"));
            raca.setForca(this.result.getInt("forca"));
            raca.setDestreza(this.result.getInt("destreza"));
            raca.setConstituicao(this.result.getInt("constituicao"));
            raca.setInteligencia(this.result.getInt("inteligencia"));
            raca.setSabedoria(this.result.getInt("sabedoria"));
            raca.setCarisma(this.result.getInt("carisma"));
            raca.setSistemaId(this.result.getInt("sistemaId"));
            racas.add(raca);
        }
        this.close();
        return racas;
    }
}
