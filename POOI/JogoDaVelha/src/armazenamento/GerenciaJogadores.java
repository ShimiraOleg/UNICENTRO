/*
xi
@version 0.5
@author Mateus de Oliveira Lopes
 */

package armazenamento;

import java.io.FileWriter;

public interface GerenciaJogadores {
  void adicionarJogador(String nome1, int pontuacao1, String nome2, int pontuacao2, FileWriter fw);
  
}
