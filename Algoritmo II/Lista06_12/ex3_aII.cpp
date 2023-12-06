#include <iostream>
#include <stdlib.h>
#define MAX 100
using namespace std;

void criarFuncao(float[], float);
void mediaAritmetica(float[], float);

int main()
{
    float *vetor, nAlunos;
    cout << "Insira o numero de alunos: ";
    cin >> nAlunos;
    vetor = (float*) malloc(nAlunos*sizeof(float));
    
    if(!vetor)
    {
        cout << "Erro de memória" << endl;
        return -1;
    }
    
    criarFuncao(vetor, nAlunos);
    mediaAritmetica(vetor, nAlunos);
    
    delete[] vetor;
    
    return 0;
}

void criarFuncao(float *v, float tamanho)
{
    for(int i = 0; i < tamanho; i++)
    {
        cout << "Insira a nota do aluno " << (i+1) << endl;
        cin >> v[i];
    }
}

void mediaAritmetica(float *vetor, float tamanho)
{
    float soma = 0;
    for(int i = 0; i < tamanho; i++)
    {
        soma += vetor[i];
    }
    cout << "Media Aritmetica da sala: " << soma/tamanho << endl;
}