void main(List<String> arguments) {
  List<int> intervalo = List.generate(10, (i) => (i + 1)*10);
  print(intervalo);
  print(intervalo.isEmpty);
  print(intervalo.isNotEmpty);
  print(intervalo.map((i) => i % 20 == 0 ? i * 2 : i - 5));
}
