#include <iostream>
#include <math.h>

using namespace std;

int main() {

    int A, B, C, soma;

    cin >> A >> B >> C;

    A = pow(A, 2);
    B = pow(B, 2);
    C = pow(C, 2);

    soma = A + B + C;

    cout << soma << endl;
    
    return 0;
}