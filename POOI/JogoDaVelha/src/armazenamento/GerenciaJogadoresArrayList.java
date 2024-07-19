package armazenamento;
import java.util.ArrayList;
import java.util.Map;


public class GerenciaJogadoresArrayList implements GerenciaJogadores {

  public GerenciaJogadoresArrayList() {
    
  }

  @Override
  public void adicionarJogador(String nome1, int pontuacao1) {
    
  }

  public void atualizarJogador(ArrayList<DadosArray> array) {
    Map<String, Integer> mapa = GerenciaJogadoresArquivo.criarMapaDoArquivo();
    
    for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
        DadosArray dados = new DadosArray(entry.getKey(), entry.getValue());
        array.add(dados);
    }
  }

  public void printarPontosGerais(ArrayList<DadosArray> array) {
    for (DadosArray dados : array) {
      System.out.println(dados);
    }
  }
}
