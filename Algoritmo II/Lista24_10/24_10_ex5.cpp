#include <iostream>
using namespace std;

int inverter(string*, int);

int main()
{
    string c;
    int tamanhoString;

    cout << "escreva uma palavra\n";
    getline(cin, c);
    tamanhoString = c.length();
    inverter(&c, tamanhoString);
    cout << "Quando invertida, a palavra vira: " << c << endl;

    return 0;
}

int inverter(string* palavra, int var)
{
    string aux;
    aux = *palavra;
    for(int i = 0; i < var/2; i++)
    {
        swap(aux[i], aux[var - i - 1]);
    }
    *palavra = aux;   
}