#include <iostream>
using namespace std;

int subt(int, int);

int main()
{
    int a = 50, b;
    int *p;

    cout << "a: " << a << endl;
    
    p = &a;
    cout << "escreva a constante (ou zero para fechar o loop): ";
    cin >> b;
    while(b != 0){
        *p = subt(*p, b);
        cout << "a - " << b << ": " << a << endl;
        cout << "escreva a constante (ou zero para fechar o loop): ";
        cin >> b;
    }
    return 0;
}

int subt(int num, int num2)
{
    return (num - num2);
}