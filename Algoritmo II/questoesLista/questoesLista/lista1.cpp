#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float c, f;

    cin >> c;
    
    f = (9.0 * c + 160.0) / 5.0;

    cout <<"A temperatura em celsius eh: " << c << endl;
    cout << "A temperatura em fahrenheit eh: " << f << endl; 
    return 0;
}