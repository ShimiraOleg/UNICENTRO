#include <iostream>
using namespace std;

int incrementa(int);
int decrementa(int);

int main()
{
    int a = 5;
    int *p;

    cout << "a: " << a << endl;
    
    p = &a;
    *p = incrementa(*p);
    cout << "a: " << a << endl;
    *p = decrementa(*p);
    cout << "a: " << a << endl;
    *p = decrementa(*p);
    cout << "a: " << a << endl;

    return 0;
}

int incrementa(int num)
{
    num++;
    return num;
}

int decrementa(int num)
{
    num--;
    return num;
}