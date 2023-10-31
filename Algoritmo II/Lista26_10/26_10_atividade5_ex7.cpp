#include <iostream>
using namespace std;

void inverterVetor(int*, int);
void imprimirVetor(int*, int);

int main()
{
    int n = 5;
    int v[5] = {0,2,4,6,8};
    
    cout << "Antes de inverter: " << endl;
    imprimirVetor(v, n);
    inverterVetor(v, n);
    cout << "Depois de inverter: " << endl;
    imprimirVetor(v, n);

    return 0;
}

void inverterVetor(int *vetor, int num1)
{
    int aux[5];
    for(int i = 0; i < num1; i++)
    {
        aux[num1 - i - 1] = vetor[i];
    }

    for(int i = 0; i < num1; i++)
    {
        vetor[i] = aux[i];
    }
}

void imprimirVetor(int *vetor, int num1)
{
    for(int i = 0; i < num1; i++)
    {
        cout << vetor[i] << " ";
    }
    cout << "\n";
}
