#include <iostream>
using namespace std;

int fatorial(int n)
{
    int fatorial = 1;
    
    if(n < 0)
    {
        cout << "valor invalido" << endl;
        return 0;
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

    return fatorial;
}


int main()
{
    int n;
    cin >> n;
    cout << fatorial(n) << endl;
    return 0;
}