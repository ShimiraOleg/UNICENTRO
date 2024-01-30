#include <iostream>
using namespace std;

int somaInteiro(int);

int main()
{
    int n;
    cout << "Insira um numero inteiro positivo: ";
    cin >> n;
    cout << "A soma de todos os numeros inteiros positivos ate n eh: " << somaInteiro(n) << endl;
    return 0;
}

int somaInteiro(int n)
{
    if (n == 1)
        return 1;
    else
        return somaInteiro(n-1) + n;
}