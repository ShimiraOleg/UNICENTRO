#include <iostream>
#include <iomanip>
using namespace std;

void somaIntervalo()
{
    int n, m, total = 0;
    cin >> n >> m;
    for(int i = n; i <= m; i++)
    {
        total += i;
    }
    cout << total << endl;
}

int main()
{
    somaIntervalo();
    return 0;
}