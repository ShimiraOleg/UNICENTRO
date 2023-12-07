#include <iostream>
#define MAX 100
using namespace std;

int main()
{
    int vetor[MAX] = {1,2,3,4,5};
    int tamanho = 5, *n;

    n = &vetor[0];

    for(int i = 0; i < tamanho; i++)
    {
        n = (vetor + i);
        cout << *n << endl;
    }

    return 0;
}

