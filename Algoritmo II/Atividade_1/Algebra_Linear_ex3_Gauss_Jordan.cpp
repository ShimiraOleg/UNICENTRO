#include <iostream>
#include <iomanip>
#define MAX 20
using namespace std;

int main()
{
    float matriz[MAX][MAX], resposta[MAX], aux; 
    int n;
    
    cout << setprecision(3) << fixed;

    cout << "Escreva o numero de incognitas: ";
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        cout << "escreva os elementos da linha " << i << " da matriz" << endl;
        for(int j = 1; j <= n+1; j++)
        {
            cin >> matriz[i][j];
        }
    }

    for(int i=1;i<=n;i++)
    {
        if(matriz[i][i] == 0)
        {
            cout<<"Matriz invalida!";
            exit(0);
        }
        for(int j=1;j<=n;j++)
        {
            if(i!=j)
            {
                aux = matriz[j][i]/matriz[i][i];
                for(int k = 1; k <= n+1; k++)
                {
                    matriz[j][k] = matriz[j][k] - aux*matriz[i][k];
                }
            }
        }
    }
    for(int i=1;i<=n;i++)
    {
        resposta[i] = matriz[i][n+1]/matriz[i][i];
    }
    
    cout<< endl<<"Resposta: "<< endl;
	for(int i = 1; i <= n; i++)
	{
	    cout<<"x["<< i<<"] = "<< resposta[i]<< endl;
	}
    return 0;
}