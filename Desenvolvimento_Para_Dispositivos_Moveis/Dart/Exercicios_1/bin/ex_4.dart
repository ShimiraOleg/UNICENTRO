void main(){
  int A = 4;
  int B = 17;
  int C = 3;
  List<int> resultado = [A,B,C];
  resultado.sort((D,E) => E.compareTo(D));
  print(resultado);
} 