#include <iostream>
using namespace std;

int soma(int, int);

int main()
{
    int a = 5, b;
    int *p;

    cout << "a: " << a << endl;
    
    p = &a;
    cout << "escreva a constante (ou zero para fechar o loop): ";
    cin >> b;
    while(b != 0){
        *p = soma(*p, b);
        cout << "a + " << b << ": " << a << endl;
        cout << "escreva a constante (ou zero para fechar o loop): ";
        cin >> b;
    }
    return 0;
}

int soma(int num, int num2)
{
    return (num + num2);
}