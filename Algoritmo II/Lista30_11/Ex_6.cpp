#include <iostream>
using namespace std;

static int a = 10;

void incrementar();

int main()
{
    cout << "A inicial = " << a << endl;
    for(int i = 0; i < 6; i++)
    {
        incrementar();
    }
    cout << "A final = " << a << endl;
}

void incrementar()
{
    a++;
    cout << "A = " << a << endl;
}
