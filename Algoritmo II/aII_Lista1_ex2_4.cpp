#include <iostream>
#include <iomanip>
using namespace std;

float calcularVolumeEsfera(float r, float pi)
{
    float volume;
    volume = ((4 * pi * (r*r*r))/3);
    return volume;
}


int main()
{
    float r, pi = 3.1415;
    cin >> r;
    cout << fixed << setprecision(2) << calcularVolumeEsfera(r, pi) << endl;
    return 0;
}