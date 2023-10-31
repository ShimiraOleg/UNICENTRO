#include <iostream>
using namespace std;

string transformarMaiusculo(string);

int main()
{
    string palavra;
    cout << "insira uma palavra: ";
    getline(cin, palavra); 
    cout << "Ela maiusculo fica: " << transformarMaiusculo(palavra);

    return 0;
}

string transformarMaiusculo(string p)
{
    int i = 0;
    for(char c: p)
    {
        if(c >= 97 && c <= 122)
        {
            p[i] -= 32; 
        }
        i++;
    }

    return p;
}