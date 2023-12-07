#include <iostream>
using namespace std;

extern int n;

int troca_var();

int troca_var()
{
    cout << "Durante a troca 1: " << n << endl;
    n = 50;
    cout << "Durante a troca 2: " << n << endl;
}
