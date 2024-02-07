#include <iostream>
#define MAX 100
using namespace std;

int buscaSequencialRecursiva(int, int*, int);
int criarVetor(int*, int);

int main()
{
    int tamanho = 50, x, j;
    int v[MAX]; 

    criarVetor(v,tamanho);
    cout << "Defina um valor: ";
    cin >> x;
    j = buscaSequencialRecursiva(x,v,tamanho);
    if(j == -1)
    {
        cout << "O valor nao esta no vetor!" << endl;
    }
    else
    {
        cout << "j = " << j << endl;
        cout << v[j-1] << " < " << x << " <= " << v[j] << endl;
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

int buscaSequencialRecursiva(int x, int *v, int n)
{
    if (n == -1)
    {
        return -1;
    }
    else
    {
        int i = n;
        if(v[i] == x)
        {
            return i;
        }
        buscaSequencialRecursiva(x,v,i-1);
    }
}