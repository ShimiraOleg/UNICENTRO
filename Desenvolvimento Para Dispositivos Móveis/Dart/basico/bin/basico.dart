/*import 'package:basico/basico.dart' as basico;

void main(List<String> arguments) {
  print('Hello world: ${basico.calculate()}!');
  saudacoes("Mateus de Oliveira", sobrenome: "Lopes");
}

void saudacoes(String nome, {String? sobrenome = 'não informado'}){
  print('seja  bem vindo: $nome $sobrenome');
}*/

void main(List<String> arguments) {
  saudacoes("Mateus de Oliveira", sobrenome: adicionaSobrenome);
}

void adicionaSobrenome(){
  print("Lopes");
}

void saudacoes(String nome, {required Function sobrenome}){
  print('seja  bem vindo: $nome');
}