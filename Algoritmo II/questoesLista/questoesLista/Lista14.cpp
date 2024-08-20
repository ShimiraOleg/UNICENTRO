#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float SM, PR, NS;

    cin >> SM >> PR;

    NS = SM - ((PR/100.0f) * SM);

    cout << fixed << setprecision(2) << "Salario apos o reajuste = R$" << NS << endl;

    return 0;

}