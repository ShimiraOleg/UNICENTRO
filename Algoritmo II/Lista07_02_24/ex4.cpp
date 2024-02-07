#include <iostream>
#define MAX 100
using namespace std;

int buscaBinaria(int, int*, int);
int criarVetor(int*, int);

int main()
{
    int tamanho = 50, x, j;
    int v[MAX]; 

    criarVetor(v,tamanho);
    cout << "Defina um valor: ";
    cin >> x;
    j = buscaBinaria(x,v,tamanho);
    if(j == -1)
    {
        cout << "O valor nao esta no vetor!" << endl;
    }
    else
    {
        cout << "j = " << j << endl;
        cout << v[j] << " >= "<< x << endl;
        cout << "O valor " << x << " esta na "<< j <<" posicao do vetor!" << endl;
    }
    return 0;
}

int criarVetor(int *v, int n)
{
    for(int i = 0; i < n; i++)
    {
        v[i] = i+1;
    }
}

int buscaBinaria(int x, int *v, int n)
{
    int inicio = 0;
    int fim = n-1;

    while(inicio <= fim)
    {
        int meio = (inicio+fim) / 2;
        if (v[meio] == x)
        {
            return meio;
        }
        if(v[meio] < x)
        {
            inicio = meio;
        }
        else
        {
            fim = meio+1;
        }
    }
    return -1;
}

