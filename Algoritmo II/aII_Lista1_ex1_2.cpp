#include <iostream>
using namespace std;

void inteiroImparOuPar()
{
    int n;
    cin >> n;
    if (n % 2 == 0)
    {
        cout << n << " eh par" << endl;
    } 
    else if(n % 2 != 0)
    {
        cout << n << " eh impar" << endl;
    }
}

int main()
{
    inteiroImparOuPar();
    return 0;
}