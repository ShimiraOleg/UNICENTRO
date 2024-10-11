package exemplo.curso1.dao;

import java.sql.SQLException;
import exemplo.curso1.model.Estudante;

public interface IEstudante {
    public void inserir(Estudante estudante) throws SQLException;
}