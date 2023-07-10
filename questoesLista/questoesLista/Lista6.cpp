#include <iostream>

using namespace std;

int main() {

    float A, B, C;

    cin >> A >> B;
    
    C = A;
    A = B;
    B = C;

    cout << "A = " << A << endl << "B = " << B << endl;
    
    return 0;
}