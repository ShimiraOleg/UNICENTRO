#include <iostream>
using namespace std;

int potencia(int, int);

int main()
{
    int base, expoente;
    cout << "Insira a base: ";
    cin >> base;
    cout << "Insira o expoente: ";
    cin >> expoente;
    cout << "O resultado dessa potencia eh: " << potencia(base, expoente) << endl;
    return 0;
}

int potencia(int base, int expoente)
{
    if (expoente == 1)
        return base;
    else
    {
        return potencia(base, expoente - 1) * base;
    }
}