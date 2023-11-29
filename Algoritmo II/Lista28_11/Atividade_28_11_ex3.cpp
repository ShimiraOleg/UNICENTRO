#include <iostream>
#define MAX 100
using namespace std;

void parOuImpar(int*, int*, int*, int*);

int main()
{
    int vetor[MAX], vetorPar[MAX], vetorImpar[MAX];
    int total;

    cout << "Insira o tamanho do vetor: ";
    cin >> total;

    cout << "Insira os elementos do vetor: ";
    for(int i = 0; i < total; i++)
    {
        cin >> vetor[i];
    }

    parOuImpar(vetor, vetorPar, vetorImpar, &total);
    return 0;
}

void parOuImpar(int *vetor, int *vetorPar, int *vetorImpar, int *total)
{
    int tP = 0, tI = 0;
    for(int i = 0; i < *total; i++)
    {
        if(*(vetor + i) % 2 == 0)
        {
            *(vetorPar + tP) = *(vetor + i);
            tP++;
        }
        else
        {
            *(vetorImpar + tI) = *(vetor + i);
            tI++;            
        }
    }

    cout << "Vetor Par: ";
    for(int i = 0; i < tP; i++)
    {
        cout << *(vetorPar + i) << " ";
    }
    cout << "\n";

    cout << "Vetor Impar: ";
    for(int i = 0; i < tI; i++)
    {
        cout << *(vetorImpar + i) << " ";
    }
    cout << "\n";
}