import 'dart:convert';

String dadosAluno(){
  return """{
    "nome": "André Fernando",
    "sobrenome": "Tozzi",
    "idade": "23",
    "casado": true,
    "telefones": [
      {"ddd": 42, "numero": 940028922, "tipo": "celular"},
      {"ddd": 42, "numero": 997295673, "tipo": "celular"}
    ]
  }""";
}

void main(){
  Map<String, dynamic> dados = json.decode(dadosAluno());
  //print(dados);
  //print(dados['nome']);
  print(dados['telefones'][0]);
}