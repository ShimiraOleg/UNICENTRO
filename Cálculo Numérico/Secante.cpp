#include <iostream>
#include <iomanip>
#include <cmath>
#include <string.h>

using namespace std;

double funcaoMatematica(double);
double secante(double, double);

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
    } if(abs(funcaoMatematica(x1)) < precisao || abs(x1-x0) < precisao){
        raiz = x1;
    } else {
        x2 = x1;
        while(k < n && abs(funcaoMatematica(x2)) > precisao)
        {    
            k++;
            x2 = secante(x0,x1);
            raiz = x2;
            x0=x1;
            x1=x2;
        }
    }

    cout << endl << "Raiz = " << raiz << endl;
    cout << "Numero de Interacoes = " << k << endl;

    return 0;
}

double funcaoMatematica(double num)
{
    return ((pow(num,2) + num) - 6);
}

double secante(double num1, double num2)
{
    return (num2 - ((funcaoMatematica(num2)*(num2 - num1))/((funcaoMatematica(num2))-(funcaoMatematica(num1)))));
}