#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {

    float valorCotacaoDolar, real, convertido;

    cin >> valorCotacaoDolar >> real;

    convertido = real / valorCotacaoDolar;

    cout << setprecision(3) << "U$ " << convertido << endl;
    
    return 0;
}