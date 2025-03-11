package com.example.javafx_mvc;

import javax.swing.*;
import java.awt.event.ActionListener;

public class View extends JFrame {
    JTextField textFrase, textAutor;
    JLabel visorFrase,visorAutor;
    JButton button;

    public View() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BoxLayout( getContentPane(), BoxLayout.Y_AXIS));
        JLabel insiraFrase = new JLabel("Insira a frase:");
        add(insiraFrase);
        textFrase = new JTextField(8);
        add(textFrase);
        JLabel insiraAutor = new JLabel("Insira o autor:");
        add(insiraAutor);
        textAutor = new JTextField(8);
        add(textAutor);
        visorFrase = new JLabel(" ");
        add(visorFrase);
        visorAutor = new JLabel(" ");
        add(visorAutor);
        button = new JButton("Crie a citação");
        add(button);
        pack();
        setVisible(true);
    }

    public String getTextFrase() {
        return textFrase.getText();
    }

    public String getTextAutor() {
        return textAutor.getText();
    }

    public void setVisorFrase(String frase) {
        visorFrase.setText(frase);
    }

    public void setVisorAutor(String autor) {
        visorAutor.setText(autor);
    }

    public void setButtonBehavior(ActionListener buttonBehavior) {
        button.addActionListener(buttonBehavior);
    }
}