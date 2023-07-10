#include <iostream>
#include <math.h>

using namespace std;

int main() {

    int A, B, C, soma;

    cin >> A >> B >> C;

    soma = A + B + C;

    soma = pow(soma, 2);

    cout << soma << endl;
    
    return 0;
}