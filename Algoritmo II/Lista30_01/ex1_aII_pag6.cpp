#include <iostream>
using namespace std;

int somaVetor(int*, int);

int main()
{
    int v[] = {2,4,6,8}, tamanho = 4, soma;
    cout << "A soma de todos os elementos do vetor eh: " << somaVetor(v, tamanho) << endl;
    return 0;
}

int somaVetor(int *v, int tamanho)
{
    if (tamanho == 1)
        return v[0];
    else
    {
        return somaVetor(v, tamanho-1) + v[tamanho - 1];
    }
}