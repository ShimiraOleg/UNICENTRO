public class Dispositivo {
    private int codigo;
    private String nome;

    Dispositivo(int codigo, String nome) {
        this.codigo = codigo;
        this.nome = nome;
    }

    public void usar(String nomeUser)
    {
        System.out.println(nomeUser + " esta usando o dispositivo " + nome);
    }
}