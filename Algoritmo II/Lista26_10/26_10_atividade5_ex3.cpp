#include <iostream>
using namespace std;

int somaDez(int);

int main()
{
    int a;
    cout << "Escreva um numero inteiro:\n";
    cin >> a;
    cout << a << " + 10 = " << somaDez(a) << endl;
    return 0;
}

int somaDez(int num1)
{
    return (num1 + 10);
}
