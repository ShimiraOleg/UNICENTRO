module com.trabalhojava.sistemarpg {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires transitive java.sql;

    opens com.trabalhojava.sistemarpg.controller to javafx.fxml;
    exports com.trabalhojava.sistemarpg.controller;

    opens com.trabalhojava.sistemarpg.model to javafx.fxml;
    exports com.trabalhojava.sistemarpg.model;

    opens com.trabalhojava.sistemarpg.main to javafx.fxml;
    exports com.trabalhojava.sistemarpg.main;

    opens com.trabalhojava.sistemarpg.dao to javafx.fxml;
    exports com.trabalhojava.sistemarpg.dao;

}