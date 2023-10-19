#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

float calcularJuros(float, float, float);

int main()
{
    float valor, taxa, anos;

    cout << "Insira o valor, a taxa de juros anuais e o numero de anos: ";
    cin >> valor >> taxa >> anos;

    cout << fixed << setprecision(2) << "R$ " <<  calcularJuros(valor,taxa,anos) << endl;

    return 0;
}

float calcularJuros(float valor, float taxa, float anos)
{
    float resultado, taxaPlus;

    taxaPlus = (taxa/100)+1;
    resultado = valor * pow(taxaPlus,anos);

    return resultado;
}