#include <iostream>
using namespace std;

int subt(int, int);

int main()
{
    int a = 50, b = 25, resultado;
    int *p1, *p2;

    cout << "a: " << a << endl;
    cout << "b: " << b << endl;
    
    p1 = &a;
    p2 = &b;

    resultado = subt(*p1,*p2);
    
    cout << a << " - " << b << " = " << resultado; 

    return 0;
}

int subt(int num, int num2)
{
    return (num - num2);
}