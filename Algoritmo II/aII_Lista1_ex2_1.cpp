#include <iostream>
using namespace std;

int inteiroMultiploQuatro(int valor)
{

    if (valor % 4 == 0)
    {
        return true;
    } else {
        return false;
    }
}



int main()
{
    int n;
    cin >> n;
    
    if(inteiroMultiploQuatro(n) == true)
    {
        cout << n << " eh multiplo de quatro" << endl;
    }
    else if (inteiroMultiploQuatro(n) == false)
    {
        cout << n << " nao eh multiplo de quatro" << endl;
    }
    return 0;
}