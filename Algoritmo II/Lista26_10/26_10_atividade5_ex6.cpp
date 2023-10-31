#include <iostream>
using namespace std;

int subCinco(int*);

int main()
{
    int a;
    cout << "Escreva um numero inteiro:\n";
    cin >> a;
    cout << a << " - 5 = "; 
    subCinco(&a);
    cout << a << endl;
    return 0;
}

int subCinco(int *num1)
{   
    *num1 -= 5;
}
