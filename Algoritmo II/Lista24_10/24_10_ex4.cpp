#include <iostream>
using namespace std;

int contarVogais(string);

int num, *resultado;

int main()
{
    string texto;

    resultado = &num;
    cout << "Insira uma palavra" << endl;
    cin >> texto;
    cout << "Essa palavra contem " << contarVogais(texto) << " vogais" << endl;

    return 0;
}

int contarVogais(string texto)
{
    *resultado = 0;
    for(char c : texto)
    {
        if(tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u')
        {
            (*resultado)++;
        }
    }
    return num;
}
