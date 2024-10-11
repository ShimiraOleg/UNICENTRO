package exemplo.curso1.controller;

import java.sql.*;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.stage.Stage;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.TextField;
import exemplo.curso1.model.Estudante;
import exemplo.curso1.dao.EstudanteDAO;

public class IncluiEstudanteController {

    @FXML
    private Button btnConf;

    @FXML
    private TextField txtNomEst;

    @FXML
    public void initialize() {
    }

    @FXML
    private void btnConfOnAction(ActionEvent event) {
        Estudante estudante = new Estudante();
        estudante.setNome(txtNomEst.getText());

        EstudanteDAO estudanteDAO = new EstudanteDAO();
        try {
            estudanteDAO.inserir(estudante);
            Alert alert;
            alert = new Alert(AlertType.INFORMATION, "Você clicou no botão Confirmar", ButtonType.OK);
            alert.setTitle("Estudante cadastrado com sucesso!");
            alert.setHeaderText("Informação");
            alert.show();
        } catch (SQLException e1) {
            Alert alert;
            alert = new Alert(AlertType.INFORMATION, "Você clicou no botão Cancelar", ButtonType.OK);
            alert.setTitle("Estudante não foi cadastrado com sucesso!");
            alert.setHeaderText("Informação");
            alert.show();
            e1.printStackTrace();
        }
    }

    @FXML
    void btnVoltarOnAction(ActionEvent event) {
        // Obtém o stageAtual (janela que será fechada)
        Stage stageAtual = (Stage) ((Node) event.getSource()).getScene().getWindow();
        // Fecha o Stage atual
        stageAtual.close();
    }
}
