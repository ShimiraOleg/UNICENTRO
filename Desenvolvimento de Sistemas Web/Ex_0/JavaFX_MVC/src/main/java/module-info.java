module com.example.javafx_mvc {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires java.desktop;

    opens com.example.javafx_mvc to javafx.fxml;
    exports com.example.javafx_mvc;
}