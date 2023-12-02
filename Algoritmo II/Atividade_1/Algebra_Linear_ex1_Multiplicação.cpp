#include <iostream>
#define MAX 100
using namespace std;

int main()
{
    int c1, l1, c2, l2;
    int matriz1[MAX][MAX];
    int matriz2[MAX][MAX];
    int matriz3[MAX][MAX];
    bool isValido = true;

    cout << "Insira o numero de linhas de m1: ";
    cin >> l1;
    cout << "Insira o numero de colunas de m1: ";
    cin >> c1;
    
    for(int i = 0; i < l1; i++)
    {
        cout << "Escreva a linha " << i+1 << " da primeira matriz" << endl;
        for(int j = 0; j < c1; j++)
            {
                cin >> matriz1[i][j];
            }
    }

    cout << "Insira o numero de linhas de m2: ";
    cin >> l2;
    cout << "Insira o numero de colunas de m2: ";
    cin >> c2;
    
    for(int i = 0; i < l2; i++)
    {
        cout << "Escreva a linha " << i+1 << " da segunda matriz" << endl;
        for(int j = 0; j < c2; j++)
            {
                cin >> matriz2[i][j];
            }
    }
    if(c1 != l2) {
        isValido = false;
    }
    cout << "\n";
    if(isValido)
    {
        for(int i = 0; i < l1; i++)
        {
            for(int j = 0; j < c2; j++)
            {
                matriz3[i][j] = 0;
                for(int k = 0; k < l2; k++)
                {
                    matriz3[i][j] += matriz1[i][k] * matriz2[k][j];
                }
                cout << matriz3[i][j] << "\t";
            }
            cout << endl;
        }
    }
    else if (!isValido)
    {
        cout << "essa multiplicacao nao eh valida, pois o numero de colunas da matriz 1 nao eh igual ao numero de linhas da matriz 2" << endl;
    }
}
