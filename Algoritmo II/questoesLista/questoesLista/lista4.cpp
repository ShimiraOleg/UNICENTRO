#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float TEMPO, VELOCIDADE, DISTANCIA, LITROS_GASTOS;
    
    cin >> TEMPO >> VELOCIDADE;

    DISTANCIA = VELOCIDADE * TEMPO;
    LITROS_GASTOS = DISTANCIA / 12.0;

    cout << "A quantidade de litros gastos foi: " << LITROS_GASTOS << endl;
    return 0;
}