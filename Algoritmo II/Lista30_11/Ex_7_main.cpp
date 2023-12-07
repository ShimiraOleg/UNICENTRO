#include <iostream>
#include "Ex_7_var.cpp"
using namespace std;

int n = 10;

extern int troca_var();

int main()
{
    cout << "n anterior: " << n << endl;
    troca_var();
    cout << "n posterior: " << n;
    return 0;
}