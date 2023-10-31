#include <iostream>
using namespace std;

int multiplicar(int, int);

int main()
{
    int a, b;
    cout << "Escreva dois numeros inteiros:\n";
    cin >> a >> b;
    cout << a << " * " << b << " = " << multiplicar(a,b) << endl;
    return 0;
}

int multiplicar(int num1,int num2)
{
    return (num1 * num2);
}
