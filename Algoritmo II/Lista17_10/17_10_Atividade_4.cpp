#include <iostream>
using namespace std;

bool verificarTamanho(string);
bool verificarMinuscula(string);
bool verificarMaiuscula(string);
bool verificarNumeros(string);

int main()
{
    string s;
    bool hasOito, hasMaiuscula = false, hasMinuscula = false, hasNumero = false;

    cout << "Insira uma senha (min 8 char, incluindos letras maiusculas, minusculas e numeros): ";
    cin >> s;

    hasOito = (verificarTamanho(s)) ? true : false;
    hasMaiuscula = (verificarMaiuscula(s)) ? true : false;
    hasMinuscula = (verificarMinuscula(s)) ? true : false;
    hasNumero = (verificarNumeros(s)) ? true : false;

    if(hasOito && hasMaiuscula && hasMinuscula && hasNumero)
    {
        cout << "A senha eh valida" << endl;
    }
    else
    {
        cout << "A senha nao eh valida" << endl;
    }
    return 0;
}

bool verificarTamanho(string senha)
{  
    int numTotal = 0;
    
    while(senha[numTotal] != '\0')
    {
        numTotal++;
    }
    
    if(numTotal >= 8) 
    {
        return true;
    }
    else 
    {
        return false;
    }
}

bool verificarMaiuscula(string senha)
{
    int numTotal = 0;
    while(senha[numTotal] != '\0')
    {
        if(senha[numTotal] >= 65 && senha[numTotal] <= 90)
        {
            return true;
        }
        numTotal++;
    }
    return false;
}

bool verificarMinuscula(string senha)
{
    int numTotal = 0;
    while(senha[numTotal] != '\0')
    {
        if(senha[numTotal] >= 97 && senha[numTotal] <= 122)
        {
            return true;
        }
        numTotal++;
    }
    return false;
}

bool verificarNumeros(string senha)
{
    int numTotal = 0;
    while(senha[numTotal] != '\0')
    {
        if(senha[numTotal] >= 48 && senha[numTotal] <= 57)
        {
            return true;
        }
        numTotal++;
    }
    return false;
}