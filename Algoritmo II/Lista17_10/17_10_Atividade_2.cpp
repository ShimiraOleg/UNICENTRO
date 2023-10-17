#include <iostream>
using namespace std;

int verificarBissexto(int);

int main()
{
    int ano;

    cout << "Insira um ano: ";
    cin >> ano;

    if(verificarBissexto(ano) == true)
    {
        cout << "O ano eh bissexto" << endl;
    }
    else if (verificarBissexto(ano) == false)
    {
        cout << "O ano nao eh bissexto" << endl;
    }

    return 0;
}

int verificarBissexto(int ano)
{
    if(ano % 4 == 0)
    {
        if(ano % 100 == 0)
        {
            if(ano % 400 == 0)
            {
                return true;
            } else {
                return false;
            }
        } else {
            return true;
        }
    }
    else if(ano % 4 != 0)
    {
        if(ano % 400 == 0)
        {
            return true;
        } else {
        return false;
        }
    } 
}
