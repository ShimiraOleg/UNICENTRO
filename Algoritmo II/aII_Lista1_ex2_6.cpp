#include <iostream>
using namespace std;

int potencia(int b, int e)
{
    int total = 1;
    for (int i = 1; i <= e; i++)
    {
        total *= b;
    }
    return total;
}


int main()
{
    int b, e;
    cin >> b >> e;
    cout << potencia(b,e) << endl;
    return 0;
}