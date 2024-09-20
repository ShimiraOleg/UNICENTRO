#include <iostream>
#include <iomanip>
#include <cmath>
#include <string.h>

using namespace std;

float verificarIntervalo(float, float);
float funcaoMatematica(float, int);

int main()
{
    float precisao;
    float intervaloMin;
    float intervaloMax;
    int n;
    int tipo;
    int k = 0;

    float finicio;
    float meio;
    float fmeio;
    
    cout << "Insira o Intervalo Minimo: ";
    cin >> intervaloMin;
    cout << "Insira o Intervalo Maximo: ";
    cin >> intervaloMax;
    cout << "Insira a Precisao: ";
    cin >> precisao;
    cout << "Insira o Numero Maximo de Casos: ";
    cin >> n;
    cout << "Insira qual Funcao: ";
    cin >> tipo;

    if(verificarIntervalo(intervaloMax, intervaloMin) < precisao)
    {
        meio = ((intervaloMin+intervaloMax)/2);
    } else {
        while (verificarIntervalo(intervaloMax, intervaloMin) > precisao && k < n)
        {    
            k++;
            finicio = funcaoMatematica(intervaloMin, tipo);
            meio = ((intervaloMin+intervaloMax)/2);
            fmeio = funcaoMatematica(meio, tipo);
            if(finicio*fmeio < 0)
            {
                intervaloMax = meio;
            } else {
                intervaloMin = meio;
            }
        }
        
    }

    cout << endl << "Raiz = " << meio << endl;
    cout << "Numero de Interacoes = " << k << endl;

    return 0;
}

float verificarIntervalo(float max, float min)
{
    return(abs(max-min));
}

float funcaoMatematica(float num, int tipo)
{
    if(tipo == 1)
    {
        return ((pow(num,3))-10);
    }
    else if(tipo == 2)
    {
        return ((exp(-(pow(num,2))))-(cos(num)));
    }
    else
    {
        return 0;
    }
} 
//lerFuncao()
//{
//int
//}