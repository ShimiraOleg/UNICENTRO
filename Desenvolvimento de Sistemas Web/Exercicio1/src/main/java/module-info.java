module com.example.exercicio1 {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;

    opens com.example.exercicio1 to javafx.fxml;
    exports com.example.exercicio1;
}