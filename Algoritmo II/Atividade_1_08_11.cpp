#include <iostream>
#include <iomanip>
using namespace std;

int maiorNoVetor(int[], int);
float mediaNoVetor(int[], int);
int positivoNoVetor(int[], int);

int main()
{
    int n = 5;
    int vetor[n] = {-2, 2, 4, 10, 8};
    cout << "Maior no Vetor = " << maiorNoVetor(vetor, n) << endl;
    cout << fixed << setprecision(2) << "Media do Vetor = " << mediaNoVetor(vetor, n) << endl;
    cout << "Quantidade de Elementos Positivos no Vetor = " << positivoNoVetor(vetor, n) << endl;

    return 0;
}

int maiorNoVetor(int a[], int n)
{
    int aux = 0;
    for (int i = 0; i < n; i++)
    {
        if(a[i] >= aux)
        {
            aux = a[i];
        }
    }

    return aux;
}
float mediaNoVetor(int a[], int n)
{
    float aux = 0;

    for(int i = 0; i < n; i++)
    {
        aux += a[i];
    }

    return aux/5;
}
int positivoNoVetor(int a[], int n)
{
    int aux = 0;
    for(int i = 0; i < n; i++)
    {
        if(a[i] >= 0)
        {
            aux++;
        }
    }

    return aux;
}