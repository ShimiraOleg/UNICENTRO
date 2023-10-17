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
    int numBinario[10];

    while(num != 1)
    {
        int i = 0;
        if(num % 2 == 0)
        {
            num /= 2;
            cout << num << endl;
            numBinario[i] = 0;
            i++;
        }

        else if(num % 2 == 1)
        {
            num /= 2;
            cout << num << endl;
            numBinario[i] = 1;
            i++;
        }
    }
    for (int i = 10; i >= 0; i--)
    {
        cout << numBinario[i] << endl;
    }
    
    return 0;
}

