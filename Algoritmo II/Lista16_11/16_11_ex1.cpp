#include <iostream>
using namespace std;

typedef struct{
    string nome;
    int idade;
    float nota;

} Aluno;

int main()
{
    Aluno Mateus = {"Mateus Lopes", 19, 7.5f};

    cout << "Nome: " << Mateus.nome << endl;
    cout << "Idade: " << Mateus.idade << endl;
    cout << "Nota: " << Mateus.nota << endl;
    return 0;
}