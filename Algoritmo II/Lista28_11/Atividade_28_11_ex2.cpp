#include <iostream>
#define MAX 100
using namespace std;

void mesclar(int*, int*, int*, int*, int*, int*);

int main()
{
    int vetor1[MAX], vetor2[MAX], vetor3[MAX];
    int t1, t2, total = 0;

    cout << "Insira o tamanho do vetor1: ";
    cin >> t1;
    cout << "Insira o tamanho do vetor2: ";
    cin >> t2;

    cout << "Insira os elementos do vetor1: ";
    for(int i = 0; i < t1; i++)
    {
        cin >> vetor1[i];
    }

    cout << "Insira os elementos do vetor2: ";
    for(int i = 0; i < t2; i++)
    {
        cin >> vetor2[i];
    }

    mesclar(vetor1, vetor2, vetor3, &t1, &t2, &total);

    cout << "A juncao dos vetores eh: ";
    for(int i = 0; i < total; i++)
    {
        cout << vetor3[i] << " ";
    }
    cout << "\n";

    return 0;
}

void mesclar(int *vetor1, int *vetor2, int *vetor3, int *t1, int *t2, int *total)
{
    *total = *t1 + *t2;

    for(int i = 0; i < *t1; i++)
    {
        *(vetor3 + i) = *(vetor1 + i);
    }

    for(int i = 0; i < *t2; i++)
    {
        *(vetor3 + *t1 + i) = *(vetor2 + i);
    }
}