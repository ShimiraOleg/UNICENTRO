void main(){
  int somaImparMultiploTres = 0;
  int i = 0;
  while(i <= 500){
    somaImparMultiploTres += i % 3 == 0 && i % 2 == 1 ? i : 0;
    i++;
  }
  print(somaImparMultiploTres);
}