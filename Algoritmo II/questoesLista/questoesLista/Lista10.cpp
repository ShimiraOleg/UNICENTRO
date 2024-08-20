#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {

    float valorCotacaoDolar, dolar, convertido;

    cin >> valorCotacaoDolar >> dolar;

    convertido = dolar * valorCotacaoDolar;

    cout << setprecision(3) << "U$ " << convertido << endl;
    
    return 0;
}