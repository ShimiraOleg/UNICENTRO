#include <iostream>
using namespace std;

int imprimirVetor(int[], int*);

int main()
{
    int vetor[5] = {0,2,4,6,8};
    int num = 0;

    while(num < 5)
    {
        cout << imprimirVetor(vetor, &num) << " "; 
    }
    cout << "\n";

    return 0;
}

int imprimirVetor(int vetor[], int* num)
{
    *num = *num + 1;
    return vetor[*num-1];
}