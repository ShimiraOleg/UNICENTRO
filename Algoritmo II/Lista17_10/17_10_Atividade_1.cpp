#include <iostream>
using namespace std;

int somarNumerosAnteriores(int);

int main()
{
    int numero;

    cout << "Insira um numero: ";
    cin >> numero;

    cout << "A soma de todos os seus anteriores e ele mesmo eh: " << somarNumerosAnteriores(numero) << endl;

    return 0;
}

int somarNumerosAnteriores(int n)
{
    int resultado = 0;

    for(int i = 0; i <= n; i++)
    {
        resultado += i;
    }

    return resultado;
}