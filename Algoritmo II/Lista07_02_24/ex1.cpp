#include <iostream>
#define MAX 100
using namespace std;

int buscaSequencial(int, int*, int);
int criarVetor(int*, int);

int main()
{
    int tamanho = 50, x, j;
    int v[MAX]; 

    criarVetor(v,tamanho);
    cout << "Defina um valor: ";
    cin >> x;
    j = buscaSequencial(x,v,tamanho);
    if(j == -2)
    {
        cout << "O valor nao esta no vetor!" << endl;
    }
    else
    {
        cout << "j = " << j << endl;
        cout << v[j] << " < " << x << " <= " << v[j+1] << endl;
        cout << "O valor " << x << " esta na "<< j+1 <<" posicao do vetor!" << endl;
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

int buscaSequencial(int x, int *v, int n)
{
    for(int i = 0; i < n; i++)
    {
        if(v[i] == x)
        {
            return i-1;
        }
    }
    return -2;
}

