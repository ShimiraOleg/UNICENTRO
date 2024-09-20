#include <iostream>
#include <iomanip>
#include <cmath>
#include <string.h>

using namespace std;

float funcaoMatematica(float, int);

int main()
{
    double precisao;
    double x0 = 0;
    double x1 = 0;
    double raiz;
    int k = 0;
    int n;
    
    cout << "Insira a Aproximacao Inicial: ";
    cin >> x0;
    cout << "Insira a Precisao: ";
    cin >> precisao;
    cout << "Insira o Numero Maximo de Casos: ";
    cin >> n;
    
    if(abs(funcaoMatematica(x0,1)) < precisao)
    {
        raiz = x0;
    } else {
        while(k < n && abs(funcaoMatematica(x0,1)) > precisao)
        {    
            k++;
            x1 = funcaoMatematica(x0,2);
            raiz = x1;
            x0 = x1;
        }
        
    }

    cout << endl << "Raiz = " << raiz << endl;
    cout << "Numero de Interacoes = " << k << endl;

    return 0;
}

float funcaoMatematica(float num, int tipo)
{
    if(tipo == 1)
    {
        return ((pow(num,3))-(9*num)+3);
    }
    else if(tipo == 2)
    {
        return ((pow(num,3))/9.0)+(1/3.0);
    }
    else
    {
        return 0;
    }
} 