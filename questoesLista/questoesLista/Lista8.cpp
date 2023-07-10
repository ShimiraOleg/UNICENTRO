#include <iostream>
#include <math.h>

using namespace std;

int main() {

    int A, B, menos, potencia;

    cin >> A >> B;

    menos = A - B;

    potencia = pow(menos, 2);

    cout << potencia << endl;
    
    return 0;
}