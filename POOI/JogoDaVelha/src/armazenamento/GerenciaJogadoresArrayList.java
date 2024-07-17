package armazenamento;
import java.util.ArrayList;

public class GerenciaJogadoresArrayList implements GerenciaJogadores {

  public GerenciaJogadoresArrayList() {
    
  }

  @Override
  public void adicionarJogador(String nome1, int pontuacao1) {
    
  }

  public void atualizarJogador(ArrayList<DadosArray> array, String nome1, int pontuacao1) {
    array.add(new DadosArray(nome1, pontuacao1));
  }
}
