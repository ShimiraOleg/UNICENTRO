#include <iostream>
using namespace std;

int dobrar(int*);

int main()
{
    int num = 5;
    cout << "Antes da funcao: " << num << endl;
    dobrar(&num);
    cout << "Depois da funcao: " << num << endl;
    return 0;
}

int dobrar(int* var)
{
    *var = 2 * (*var);
}