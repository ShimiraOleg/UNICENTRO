#include <iostream>
using namespace std;

void fatorial()
{
    long long int n, fatorial = 1;
    cin >> n;
    
    if(n < 0)
    {
        cout << "valor invalido" << endl;
    }
    else if(n == 0 || n == 1)
    {
        fatorial = 1;
    } 
    else 
    {
        for (int i = 1; i <= n; i++)
        {
            fatorial *= i;
        }
    }

    cout << fatorial << endl;
}


int main()
{
    fatorial();
    return 0;
}