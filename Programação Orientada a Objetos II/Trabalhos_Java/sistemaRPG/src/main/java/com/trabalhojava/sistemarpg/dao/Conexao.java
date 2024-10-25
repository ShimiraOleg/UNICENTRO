package com.trabalhojava.sistemarpg.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class Conexao {
    public static Connection getConexao(String stringDeConexao, String usuario, String senha) {
        try {
            return DriverManager.getConnection(stringDeConexao, usuario, senha);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
