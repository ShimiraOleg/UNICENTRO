#include <iostream>
#include <iomanip>
#include <cmath>
#include <string.h>

using namespace std;

double funcaoMatematica(double);
double regulaFalsi(double, double);

int main()
{
    double precisao;
    double x0 = 0;
    double x1 = 0;
    double x2 = 0;
    double raiz;
    int k = 0;
    int n;
    
    cout << "Insira a Primeira Aproximacao Inicial: ";
    cin >> x0;
    cout << "Insira a Segunda Aproximacao Inicial: ";
    cin >> x1;
    cout << "Insira a Precisao: ";
    cin >> precisao;
    cout << "Insira o Numero Maximo de Casos: ";
    cin >> n;
    
    if(abs(funcaoMatematica(x0)) < precisao){
        raiz = x0;
    } if(abs(funcaoMatematica(x1)) < precisao){
        raiz = x1;
    } else {
        x2 = x1;
        while(k < n && abs(funcaoMatematica(x2)) > precisao)
        {    
            k++;
            x2 = regulaFalsi(x0,x1);
            raiz = x2;
            if((funcaoMatematica(x0)*funcaoMatematica(x2)) > 0)
            {
                x0=x2;
            } else {
                x1=x2;
            }
        }
    }

    cout << endl << "Raiz = " << raiz << endl;
    cout << "Numero de Interacoes = " << k << endl;

    return 0;
}

double funcaoMatematica(double num)
{
    return ((pow(num,3) - (9*num)) + 3);
}

double regulaFalsi(double num1, double num2)
{
    return ((num1*(funcaoMatematica(num2))-(num2*(funcaoMatematica(num1))))/((funcaoMatematica(num2))-(funcaoMatematica(num1))));
}