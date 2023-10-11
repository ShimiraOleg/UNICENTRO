#include <iostream>
using namespace std;

int inteiroImparOuPar(int valor)
{
    if (valor % 2 == 0)
    {
        return true;
    } 
    else if(valor % 2 != 0)
    {
        return false;
    }
}

int main()
{
    int n;
    cin >> n;
    inteiroImparOuPar(n);
    if(inteiroImparOuPar(n) == true)
    {
        cout << n << " eh par" << endl;
    }
    else if(inteiroImparOuPar(n) == false)
    {
        cout << n << " eh impar" << endl;
    }
    return 0;
}