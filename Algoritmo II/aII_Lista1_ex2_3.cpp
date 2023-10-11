#include <iostream>
using namespace std;

int somaIntervalo(int n, int m)
{
    int total = 0;
    for(int i = n; i <= m; i++)
    {
        total += i;
    }
    return total;
}

int main()
{
    int n, m;
    cin >> n >> m;
    cout << somaIntervalo(n, m) << endl;
    return 0;
}