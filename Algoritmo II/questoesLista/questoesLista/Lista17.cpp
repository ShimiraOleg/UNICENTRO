#include <iostream>

using namespace std;

int main()
{
    float velocidade, distancia, tempo;

    cin >> distancia >> tempo;
    
    velocidade = (distancia * 1000)/(tempo * 60);

    cout << "A velocidade em m/s eh de: " << velocidade << " m/s" << endl;

    return 0;

}