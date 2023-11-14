#include <iostream>
#include <iomanip>
using namespace std;

typedef struct
{
    int hora;
    int minutos;
} Horario;

typedef struct
{
    int dia;
    int mes;
    int ano;
} Data;

typedef struct
{
    Data data;
    Horario horario;
    string compromisso;
} Compromisso;

void imprimir(Compromisso *comp)
{
    cout << "Data do evento: " << setfill('0') << setw(2) << comp->data.dia;
    cout << setfill('0') << "/" << setw(2) << comp->data.mes << "/";
    cout << setfill('0') << setw(4) << comp->data.ano << endl;

    cout << "Horario do evento: " <<setfill('0') << setw(2) << comp->horario.hora;
    cout << setfill('0') << ":" << setw(2) << comp->horario.minutos << endl;

    cout << comp->compromisso << endl;
}

int main()
{
    Compromisso eventos[2];
    eventos[0] = {14, 11, 2023, 17, 25, "Jogar o modo Brodota para o jogo Dota 2 com os crias"};
    eventos[1] = {17, 11, 2023, 20, 30, "Jogar RPG com os crias"};
    for(int i = 0; i < 2; i++)
    {
        imprimir(&eventos[i]);
        cout << endl;
    }
    return 0;
}