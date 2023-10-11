#include <iostream>
using namespace std;

void inteiroMultiploQuatro()
{
    int n;
    cin >> n;
    if (n % 4 == 0)
    {
        cout << n << " eh multiplo de quatro" << endl;
    } else {
        cout << n << " nao eh multiplo de quatro" << endl;
    }
}



int main()
{
    inteiroMultiploQuatro();
    return 0;
}