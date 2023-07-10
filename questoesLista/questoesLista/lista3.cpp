#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    float vol, r, h;
    
    cin >> r >> h;

    vol = 3.1415 * pow(r,2) * h;

    cout << "O volume eh: " << vol << endl;
    return 0;
}