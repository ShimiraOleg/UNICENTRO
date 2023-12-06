#include <iostream>
#include <stdlib.h>
#define MAX 100
using namespace std;

void criarFuncao(int[], int);
void printFuncao(int[], int);

int main()
{
    int *vetor, tamanho;
    cin >> tamanho;
    vetor = (int*) malloc(tamanho*sizeof(int));
    
    if(!vetor)
    {
        cout << "Erro de memória" << endl;
        return -1;
    }
    
    criarFuncao(vetor, tamanho);
    printFuncao(vetor, tamanho);
    
    delete[] vetor;
    
    return 0;
}

void criarFuncao(int *v, int tamanho)
{
    for(int i = 0; i < tamanho; i++)
    {
        *(v + i) = i;
    }
}

void printFuncao(int *vetor, int tamanho)
{
        for(int i = 0; i < tamanho; i++)
    {
        cout << *(vetor + i) << ", ";
    }
    cout << "\n";
}