module exemplo.curso1 {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires transitive java.sql;

    opens exemplo.curso1.controller to javafx.fxml;
    exports exemplo.curso1.controller;

    opens exemplo.curso1.model to javafx.fxml;
    exports exemplo.curso1.model;

    opens exemplo.curso1.main to javafx.fxml;
    exports exemplo.curso1.main;

    opens exemplo.curso1.dao to javafx.fxml;
    exports exemplo.curso1.dao;

}