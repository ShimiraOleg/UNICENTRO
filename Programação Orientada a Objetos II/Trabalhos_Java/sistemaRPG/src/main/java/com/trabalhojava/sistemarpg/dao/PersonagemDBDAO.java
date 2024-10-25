package com.trabalhojava.sistemarpg.dao;

import com.trabalhojava.sistemarpg.model.Personagem;
import com.trabalhojava.sistemarpg.model.PersonagemSistema;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class PersonagemDBDAO implements PersonagemDAO, IConst {
    private String sql;
    private Connection connection;
    private PreparedStatement statement;
    private ResultSet result;

    public PersonagemDBDAO() {
    }

    private void open() throws SQLException {
        this.connection = Conexao.getConexao("jdbc:postgresql://localhost:5432/sistemarpg", "postgres", "postgres");
    }

    private void close() throws SQLException {
        this.connection.close();
    }

    public void insere(Personagem personagem) throws SQLException {
        this.open();
        this.sql = "INSERT INTO personagem(personagemId,nome,descricao,urlImg,nivel,forca,destreza,constituicao,inteligencia,sabedoria,carisma) VALUES(?,?,?,?,?,?,?,?,?,?,?)";
        this.statement = this.connection.prepareStatement(this.sql);
        this.statement.setInt(1, personagem.getPersonagemId());
        this.statement.setString(2, personagem.getNome());
        this.statement.setString(3, personagem.getDescricao());
        this.statement.setString(4, personagem.getUrlImg());
        this.statement.setInt(5, personagem.getNivel());
        this.statement.setInt(6, personagem.getForca());
        this.statement.setInt(7, personagem.getDestreza());
        this.statement.setInt(8, personagem.getConstituicao());
        this.statement.setInt(9, personagem.getInteligencia());
        this.statement.setInt(10, personagem.getSabedoria());
        this.statement.setInt(11, personagem.getCarisma());
        this.statement.executeUpdate();
        this.close();
    }

    public void atualizar(Personagem personagem) throws SQLException {
        this.open();
        this.sql = "UPDATE personagem SET nome=?, descricao=?, urlImg=?, nivel=?, forca=?, destreza=?, constituicao=?, inteligencia=?, sabedoria=?, carisma=? WHERE personagemId=?";
        this.statement = this.connection.prepareStatement(this.sql);
        this.statement.setString(1, personagem.getNome());
        this.statement.setString(2, personagem.getDescricao());
        this.statement.setString(3, personagem.getUrlImg());
        this.statement.setInt(4, personagem.getNivel());
        this.statement.setInt(5, personagem.getForca());
        this.statement.setInt(6, personagem.getDestreza());
        this.statement.setInt(7, personagem.getConstituicao());
        this.statement.setInt(8, personagem.getInteligencia());
        this.statement.setInt(9, personagem.getSabedoria());
        this.statement.setInt(10, personagem.getCarisma());
        this.statement.setInt(11, personagem.getPersonagemId());
        this.statement.executeUpdate();
        this.close();

    }

    public void remover(Personagem personagem) throws SQLException {
        this.open();
        this.sql = "DELETE FROM PERSONAGEM WHERE personagemId=?";
        this.statement = connection.prepareStatement(this.sql);
        this.statement.setInt(1,personagem.getPersonagemId());
        this.statement.executeUpdate();
        this.close();
    }

    public List<Personagem> listar() throws SQLException {
        this.open();
        this.sql = "SELECT * FROM Personagem";
        this.statement = this.connection.prepareStatement(this.sql);
        this.result = this.statement.executeQuery();
        ArrayList<Personagem> personagens = new ArrayList<>();

        while (this.result.next()) {
            Personagem personagem = new Personagem();
            personagem.setPersonagemId(this.result.getInt("personagemId"));
            personagem.setNome(this.result.getString("nome"));
            personagem.setDescricao(this.result.getString("descricao"));
            personagem.setUrlImg(this.result.getString("urlImg"));
            personagem.setNivel(this.result.getInt("nivel"));
            personagem.setForca(this.result.getInt("forca"));
            personagem.setDestreza(this.result.getInt("destreza"));
            personagem.setConstituicao(this.result.getInt("constituicao"));
            personagem.setInteligencia(this.result.getInt("inteligencia"));
            personagem.setSabedoria(this.result.getInt("sabedoria"));
            personagem.setCarisma(this.result.getInt("carisma"));
            personagens.add(personagem);
        }
        this.close();
        return personagens;
    }
}
