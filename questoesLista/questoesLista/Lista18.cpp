#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    float volume, raio;

    cin >> raio;

    volume  = (4/3) * 3.14159f * (pow(raio,3));

    cout << fixed << setprecision(2) << "o volume da esfera eh: " << volume << endl;

    return 0;

}