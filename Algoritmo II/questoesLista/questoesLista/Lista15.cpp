#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    float area, raio;
    
    cin >> raio;
    
    area = 3.14159265f * (pow(raio, 2));

    cout << fixed << setprecision(2) << "A area eh: " << area << endl;

    return 0;

}