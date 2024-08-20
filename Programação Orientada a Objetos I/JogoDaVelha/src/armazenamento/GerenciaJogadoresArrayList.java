package armazenamento;
import java.util.ArrayList;
import java.util.Map;

/**
 Implementação da interface GerenciaJogadores para ler o arquivo de texto e colocar
 as informações em uma ArrayList.
 @version 1.0
 @author Yan Gabriel Reis Oliveira
 */
public class GerenciaJogadoresArrayList implements GerenciaJogadores {

  public GerenciaJogadoresArrayList() {
    
  }

  @Override
  public void adicionarJogador(String nome1, int pontuacao1) {
    
  }

  /**
  * Este metodo percorre o mapa criado a partir do arquivo de texto e coloca as informações em um ArrayList.
    @param array ArrayList que irá armazenar as informações.
    @return void
  */
  public void atualizarJogador(ArrayList<DadosArray> array) {
    Map<String, Integer> mapa = GerenciaJogadoresArquivo.criarMapaDoArquivo();
    
    for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
        DadosArray dados = new DadosArray(entry.getKey(), entry.getValue());
        array.add(dados);
    }
  }

  /**
   * Este metodo percorre o ArrayList e imprime as informações contidas nele.
   * @param array ArrayList que contém as informações.
   * @return void
   */
  public void printarPontosGerais(ArrayList<DadosArray> array) {
    for (DadosArray dados : array) {
      System.out.println(dados);
    }
  }
}
