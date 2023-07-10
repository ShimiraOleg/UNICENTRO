#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float c, f;

    cin >> f;
    
    c = (f - 32) * (5.0 / 9.0);

    cout << "A temperatura em fahrenheit eh: " << f << endl; 
    cout <<"A temperatura em celsius eh: " << c << endl;
    return 0;
}