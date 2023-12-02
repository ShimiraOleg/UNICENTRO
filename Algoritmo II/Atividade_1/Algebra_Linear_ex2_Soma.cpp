#include <iostream>
#define MAX 20
using namespace std;

int main()
{
    int c, l;
    int matriz1[MAX][MAX];
    int matriz2[MAX][MAX];
    int matriz3[MAX][MAX];

    cout << "Insira o numero de colunas das matrizes: ";
    cin >> c;
    cout << "Insira o numero de linhas das matrizes: ";
    cin >> l;
    for(int i = 0; i < l; i++)
    {
        cout << "Escreva os elementos da linha " << i+1 << " da primeira matriz" << endl;
        for(int j = 0; j < c; j++)
            {
                cin >> matriz1[i][j];
            }
    }

    for(int i = 0; i < l; i++)
    {
        cout << "Escreva os elementos da linha " << i+1 << " da segunda matriz" << endl;
        for(int j = 0; j < c; j++)
            {
                cin >> matriz2[i][j];
            }
    }
    cout << "\n";

    for(int i = 0; i < l; i++)
    {
        for(int j = 0; j < c; j++)
        {
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j];
            cout << matriz3[i][j] << "\t";
        }
        cout << endl;
    }
}
