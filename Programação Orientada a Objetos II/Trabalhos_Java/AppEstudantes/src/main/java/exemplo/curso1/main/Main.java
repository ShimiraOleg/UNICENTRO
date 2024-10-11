package exemplo.curso1.main;

import java.io.IOException;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        // Cria um objeto responsável por carregar e analisar sintaticamente um arquivo .fxml
        FXMLLoader principal = new FXMLLoader(getClass().getResource("/exemplo/curso1/view/Menus.fxml"));
        // carrega o arquivo fxml e constrói a árvore de objetos da interface gráfica
        Parent root = principal.load();
        Scene scene = new Scene(root);
        stage.setTitle("Estudantes");
        stage.setScene(scene);
        // define que stage não pode ser redimensionado pelo usuário
        stage.setResizable(false);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
