package exemplo.curso1.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class TelaVaziaController {

    @FXML
    public void initialize() {
    }

    @FXML
    private Button btnVoltar;

    @FXML
    void btnVoltarOnAction(ActionEvent event) {
        // Obtém o stageAtual (janela que será fechada)
        ((Stage) ((Node) event.getSource()).getScene().getWindow()).close();
    }
}