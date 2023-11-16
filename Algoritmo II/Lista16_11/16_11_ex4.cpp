#include <iostream>
using namespace std;

typedef struct{
    string nome;
    int idade;
    float nota;

} Aluno;

typedef struct
{
    string curso;
    string coordenador;
    Aluno estudante;
} Curso;


void criarRegistro(Curso *a)
{
    cout << "Insira sua idade: ";
    cin >> a->estudante.idade;
    cin.get();
    cout << "Insira seu nome: ";
    getline(cin,a->estudante.nome);
    cout << "Insira seu curso: ";
    getline(cin,a->curso);
    cout << "Insira o coordenador desse curso: ";
    getline(cin,a->coordenador);
    cout << "Insira sua nota: ";
    cin >> a->estudante.nota;
}

void imprimirRegistro(Curso *a)
{
    cout << "Nome: " << a->estudante.nome << endl;
    cout << "Idade: " << a->estudante.idade << endl;
    cout << "Nota: " << a->estudante.nota << endl;
    cout << "Curso: " << a->curso << endl;
    cout << "Coordenador do Curso: " << a->coordenador << endl;
}
int main()
{
    Curso unicentro;

    criarRegistro(&unicentro);
    cout << endl;
    imprimirRegistro(&unicentro);
    cout << endl;
    return 0;
}