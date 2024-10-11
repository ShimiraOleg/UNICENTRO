package exemplo.curso1.dao;

import java.sql.*;
import exemplo.curso1.model.*;

public class EstudanteDAO implements IEstudante, IConst {
    private String sql;

    public void inserir(Estudante estudante) throws SQLException {
        sql = "INSERT INTO estudante (nome) VALUES (?)";

        try (Connection conexao = Conexao.getConexao(Conexao.stringDeConexao, Conexao.usuario, Conexao.senha);
             PreparedStatement pstmt = conexao.prepareStatement(sql)) {
            pstmt.setString(1, estudante.getNome());
            pstmt.executeUpdate();
        }
    }
}