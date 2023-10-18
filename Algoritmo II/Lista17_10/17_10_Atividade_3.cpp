#include <iostream>
using namespace std;

int transformarBinario(int);

int main()
{
    int n;

    cout << "Insira um numero inteiro positivo: ";
    cin >> n;

    transformarBinario(n);

    return 0;
}

int transformarBinario(int num)
{
    int numBinario[32];
    int i = 0;

    while(num > 0)
    {
        numBinario[i] = num % 2;
        num /= 2;
        i++;
    }
    for (int j = i - 1; j >= 0; j--)
    {
        cout << numBinario[j];
    }
    cout << endl;
    
    return 0;
}
