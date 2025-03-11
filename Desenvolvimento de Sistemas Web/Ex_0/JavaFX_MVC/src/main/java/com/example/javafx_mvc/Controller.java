package com.example.javafx_mvc;

import javafx.scene.Scene;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Controller {
    Model model;
    View view;

    public Controller(Model aModel, View aView) {
        model = aModel;
        view = aView;
        view.setButtonBehavior(new ButtonBehavior());
    }

    class ButtonBehavior implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            model.setFraseAutor(view.getTextFrase(), view.getTextAutor());
            model.embelezarFrase();
            model.dividirAutor();
            String autor = model.getAutorCitacao();
            String frase = view.getTextFrase();
            view.setVisorFrase(frase);
            view.setVisorAutor(autor);
        }
    }

    public static void main(String[] args) {
        View aView = new View();
        Model aModel = new Model();
        Controller aController = new Controller(aModel, aView);
    }
}