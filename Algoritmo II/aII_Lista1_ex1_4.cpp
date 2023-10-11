#include <iostream>
#include <iomanip>
using namespace std;

void calcularVolumeEsfera()
{
    float r, volume, pi = 3.1415;
    cin >> r;
    volume = ((4 * pi * (r*r*r))/3);
    cout << fixed << setprecision(2) << volume << endl;
}


int main()
{
    calcularVolumeEsfera();
    return 0;
}