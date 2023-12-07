#include <iostream>
using namespace std;

bool maiorOuMenor(int, int, bool*);

int main()
{
    int a = 10, b = 25, resultado;
    int *p1, *p2;
    bool isMaior, isIgual = false;

    cout << "insira o valor de a: ";
    cin >> a;
    cout << "insira o valor de b: ";
    cin >> b;

    p1 = &a;
    p2 = &b;

    isMaior = maiorOuMenor(*p1,*p2,&isIgual);
    
    if(!isIgual)
    {
        if(isMaior) 
        {
            cout << "A eh maior que B" << endl;
        }
        else if (!isMaior) 
        {
            cout << "A eh menor que B" << endl;
        }
    }
    else if(isIgual)
    {
        cout << "A eh igual a B" << endl;
    }    

    return 0;
}

bool maiorOuMenor(int num, int num2, bool *isI)
{
    
    if(num > num2) {
        return true;
    }
    else if (num < num2) { 
        return false;
    }
    else if (num = num2) {
        *isI = true;
        return false;
    }
}