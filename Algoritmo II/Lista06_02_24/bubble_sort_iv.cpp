#include <iostream>
#define MAX 100
using namespace std;

int trocaBubble(int*, int);
int imprimeVetor(int*, int);

int main()
{
    int v[MAX] = {7,5,5,3,9};
    int tamanho = 5;

    cout << "Antes do Bubble Sort: ";
    imprimeVetor(v, tamanho);
    trocaBubble(v, tamanho);
    cout << "Depois do Bubble Sort: ";
    imprimeVetor(v, tamanho);

    return 0;
}

int imprimeVetor(int *v, int n)
{
        for(int i = 0; i < n; i++)
    {
        cout << v[i] << " ";
    }
    cout << "\n";
}

int trocaBubble(int *v, int n)
{
    if (n == 1) 
        return 0; 
  
    int counter = 0; 
    for (int i=0; i<n-1; i++)
    {
        if (v[i] > v[i+1])
        { 
            swap(v[i], v[i+1]); 
            counter++; 
        } 
    }
    if (counter==0) 
        return 0; 

    trocaBubble(v, n-1); 
} 