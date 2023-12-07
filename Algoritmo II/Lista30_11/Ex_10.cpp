#include <iostream>
#define MAX 100
using namespace std;

int main()
{
    int a = 5, b = 10;
    int *tA, *tB;

    tA = &a;
    tB = &b;

    if(tA > tB)
    {
        cout << "O endereco de A eh maior que o de B" << endl;
    }
    else if(tA < tB)
    {
        cout << "O endereco de B eh maior que o de A" << endl;
    }

    return 0;
}

