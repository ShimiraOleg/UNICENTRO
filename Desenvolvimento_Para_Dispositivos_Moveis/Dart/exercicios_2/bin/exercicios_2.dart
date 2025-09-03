class Pessoa {
  String nome;
  int idade;
  
  Pessoa(this.nome, this.idade);
}

var numerosPares = (List<int> numeros) {
  List<int> pares = [];
  for(int numero in numeros){
    if(numero % 2 == 0){
      pares.add(numero);
    }
  }
  return pares;
};

void main(List<String> arguments) {
  //1
  List<String> frutas = ['Maça', 'Acerola', 'Melancia', 'Tomate', 'Manga'];
  print(frutas);
  //2
  print(frutas[2]);
  //3
  frutas.add('laranja');
  print(frutas);
  frutas.remove('Maça');
  print(frutas);
  //4
  for(int i = 0; i < frutas.length; i++){
    print(frutas[i].toUpperCase());
  }
  //5
  for(String fruta in frutas){
    print(fruta.toLowerCase());
  }
  //6
  List<String?> frutasComA = [];
  for(String fruta in frutas){
    if(fruta.startsWith("A")){
      frutasComA.add(fruta);
    }
  }
  print(frutasComA);
  //7
  Map<int, String> precosFrutas = {
    2: 'Maça', 3: 'Acerola', 17: 'Melancia', 4: 'Tomate', 10: 'Manga' 
  };
  print(precosFrutas);
  //8
  for(int preco in precosFrutas.keys){
    print('${precosFrutas[preco]} = R\$ $preco,00');
  }
  //9
  List<int> listaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  print('Números originais: $listaNum');
  print('Números pares: ${numerosPares(listaNum)}');
  //10
  List<Pessoa> pessoas = [Pessoa('João', 25), Pessoa('Maria', 17), Pessoa('Pedro', 30), Pessoa('Ana', 16), Pessoa('Carlos', 22)];
  print('Pessoas maiores de idade:');
  for(Pessoa pessoa in pessoas){
    if(pessoa.idade >= 18){
      print(pessoa.nome);
    }
  }
}
