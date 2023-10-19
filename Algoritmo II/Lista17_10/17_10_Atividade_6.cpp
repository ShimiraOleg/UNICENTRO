#include <iostream>
using namespace std;
#define max 999

int ordenarVetor(int[], int);

int main()
{
    int n[max], i = 0, var;
    

    cout << "Insira todos os numeros do vetor (digite 0 para parar): ";
    while(var != 0)
    {
        cin >> var;
        n[i] = var;
        i++;
    }

    ordenarVetor(n, i);

    return 0;
}

int ordenarVetor(int num[], int tamanho)
{
    int troca;
    for(int j = 0; j < tamanho; j++)
    {
        for(int k = j+1; k < tamanho; k++)
        {
            if(num[j] > num[k])
            {
                troca = num[j];
                num[j] = num[k];
                num[k] = troca;
            }
        }   
    }

    for(int j = 1; j < tamanho; j++)
    {
        cout << num[j] << " ";
    }
    cout << endl;
}