#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float pe, metro;

    cin >> pe;

    metro = pe * 0.3048f;

    cout << fixed << setprecision(2) << pe << " pes em metros sao " << metro << " m" << endl;

    return 0;

}