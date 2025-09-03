void main(){
  int num = 100;
  while(num <= 200){
    int resultado = num % 2 == 1 ? num : 0;
    if(resultado != 0){
      print(resultado);
    }
    num++;
  }
}