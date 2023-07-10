#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float pres, valor, tax, tempo;
    cin >> valor >> tax >> tempo;

    pres = valor + (valor * (tax / 100) * tempo);

    cout << "O valor da prestacao foi de R$: " << pres << endl;
    return 0;
}