#include <iostream>
using namespace std;

void potencia()
{
    int b, e, total = 1;
    cin >> b >> e;
    for (int i = 1; i <= e; i++)
    {
        total *= b;
    }
    cout << total << endl;
}


int main()
{
    potencia();
    return 0;
}