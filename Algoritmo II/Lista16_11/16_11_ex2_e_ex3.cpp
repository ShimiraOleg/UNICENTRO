#include <iostream>
using namespace std;

typedef struct{
    string nome;
    int idade;
    float nota;

} Aluno;

void criarRegistro(Aluno *a)
{
    cout << "Insira sua idade: ";
    cin >> a->idade;
    cin.get();
    cout << "Insira seu nome: ";
    getline(cin,a->nome);
    cout << "Insira sua nota: ";
    cin >> a->nota;
}

void imprimirRegistro(Aluno *a)
{
    cout << "Nome: " << a->nome << endl;
    cout << "Idade: " << a->idade << endl;
    cout << "Nota: " << a->nota << endl;
}
int main()
{
    Aluno alunos[3];

    for(int i = 0; i < 3; i++)
    {
        criarRegistro(&alunos[i]);
    }
    cout << endl;
    for (int i = 0; i < 3; i++)
    {
        imprimirRegistro(&alunos[i]);
        cout << endl;
    }

    return 0;
}