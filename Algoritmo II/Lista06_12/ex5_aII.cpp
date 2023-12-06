#include <iostream>
#include <stdlib.h>
#define MAX 100
using namespace std;

typedef struct{
    string nome;
    int serie;
    float nota;
} Aluno;

void criarFuncao(Aluno[], int);
void mediaAritmetica(Aluno[], int);

int main()
{
    //Aluno *vetor; 
    int nAlunos;
    cout << "Insira o numero de alunos: ";
    cin >> nAlunos;
    Aluno *vetor = new Aluno[nAlunos];
    
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

void criarFuncao(Aluno *v, int tamanho)
{
    cout << tamanho;
    for(int i = 0; i < tamanho; i++)
    {
        cin.get();
        cout << "Insira o nome do aluno " << (i+1) << endl;
        getline(cin, v[i].nome);
        cout << "Insira a serie do aluno " << (i+1) << endl;
        cin >> v[i].serie;
        cout << "Insira a nota do aluno " << (i+1) << endl;
        cin >> v[i].nota;
    }
}

void mediaAritmetica(Aluno *vetor, int tamanho)
{
    float soma = 0, aux;
    for(int i = 0; i < tamanho; i++)
    { 
        soma += vetor[i].nota;
    }
    cout << "Media Aritmetica da sala: " << soma/tamanho << endl;
}