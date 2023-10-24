#include <iostream>
using namespace std;

void troca(int, int);

int main()
{
    int a = 5, b = 10;

    cout << "Valor de A: " << a << "\nValor de B: " << b << endl;
    troca(a, b);

    return 0;
}

void troca(int num1, int num2)
{
    int *p_troca, soma;
    soma = num1+num2;
    p_troca = &soma;
    num1 = *p_troca - num1;
    num2 = *p_troca - num2;


    cout << "Novo valor de A: " << num1 << "\nNovo valor de B: " << num2 << endl;
}