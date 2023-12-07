#include <iostream>

using namespace std;

int incrementa(int);

int main()
{
    int register num = 0;
    
    cout << "Valor Inicial: " << num;
    
    cout << "Primeira chamada da funcao - num = " << incrementa(num) << endl;
    cout << "Segunda chamada da funcao - num = " << incrementa(num) << endl;
    cout << "Terceira chamada da funcao - num = "<< incrementa(num) << endl;

    cout << "Valor final: " << num;

    return 0;
}

int incrementa(int var)
{   
    var++;
    return var;
}