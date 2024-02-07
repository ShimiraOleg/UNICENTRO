#include <iostream>
#define MAX 100
using namespace std;

int buscaSoma(int, int*, int, int*, int*);
int criarVetor(int*, int);

int main()
{
    int tamanho = 50, x, i, j, k;
    int v[MAX]; 

    criarVetor(v,tamanho);
    cout << "Defina um valor: ";
    cin >> x;
    k = buscaSoma(x,v,tamanho, &i, &j);
    if(k == -1)
    {
        cout << "Nao existe uma soma de dois valores dentro desse vetor que resultem em " << x << endl;
    }
    else
    {
        cout << "O valor dos vetores v[" << i << "] e v[" << j <<"] eh igual a " << x << endl;
        cout << v[i] << " + " << v[j] << " = " << x << "\n";
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

int buscaSoma(int x, int *v, int n, int *a, int *b)
{
    *a = 0;
    *b = n-1;

    while(*a != *b)
    {
        if((v[*a] + v[*b]) == x)
            return 0;
        if((v[*a] + v[*b]) > x)
            *b = (*b - 1);
        if((v[*a] + v[*b]) < x)
            *a = (*a + 1);
    }
    return -1;
}
