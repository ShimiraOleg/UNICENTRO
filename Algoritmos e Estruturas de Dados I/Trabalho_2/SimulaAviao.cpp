#include <iostream>
#include <chrono>
#include <ctime>
#include <thread>
using namespace std;
using namespace std::this_thread;
using namespace std::chrono_literals;
#include "FilaPrioridadesLEAviao.h"

void imprimePistaDePouso(int,char,int);

int main(void)
{
    node *chegadaDeAvioes, *filaPrioridade;
    int tempo, aviao, idAviao, idRand,prioridade, i, aviaoNaPista[3], quantAvioes = 0;
    char tipo, tipoNaPista[3], tipoRand;;
    bool isVazia = false, isPistaVazia = false;

    srand(time(NULL));
    
    chegadaDeAvioes = inicializaFP(chegadaDeAvioes);
    filaPrioridade = inicializaFP(filaPrioridade);

    for(int i = 0; i < 50; i++)
    {
        idRand = (rand() % 3)+1;
        if(idRand == 1 || idRand == 2)
            tipoRand = 'P';
        else
            tipoRand = 'D';    
        chegadaDeAvioes = insereFilaChegada(chegadaDeAvioes, 100+i, tipoRand, idRand);
    }   

    cout << "Avioes esperando instrucoes:\n";
    exibe(chegadaDeAvioes);
    sleep_for(1s);
    for(tempo = 1; !isVazia || (tempo%2); tempo++)
    {
        system("clear");
        cout << "\n__________________________________________" << endl;
        cout << "           " << "Unidade de Tempo: " << tempo << "           \n" << endl;
        sleep_for(0.25s);
        for (aviao = 1; aviao <= 4; aviao++){
			if (!verificaSeVazia(chegadaDeAvioes)){
				chegadaDeAvioes = removeFP(chegadaDeAvioes, &idAviao, &tipo, &prioridade);
				filaPrioridade = insereFP(filaPrioridade, idAviao, tipo, prioridade);
			}
		}
        cout << "FILA DE AVIOES ESPERANDO:\n";
        if(!verificaSeVazia(filaPrioridade))
            exibe(filaPrioridade);
        else
            cout << "SEM AVIOES ESPERANDO PARA POUSAR/DECOLAR\n";

        if ((tempo%2) && (!isVazia)){
			cout << endl;
            for (i = 1; i <= 3; i++){
				if (filaPrioridade != NULL){
					filaPrioridade = removeFP(filaPrioridade, &idAviao, &tipo, &prioridade);
                    aviaoNaPista[i-1] = idAviao;
                    tipoNaPista[i-1] = tipo;
                    quantAvioes++;
                    imprimePistaDePouso(i, tipo, idAviao);
				}
			}
			if (!verificaSeVazia(filaPrioridade)){
                sleep_for(0.25s);
				cout << endl << "FILA DE AVIOES ESPERANDO:\n";
			    exibe(filaPrioridade);
			}
            else
            {
              	sleep_for(0.25s);
                cout << endl << "SEM AVIOES NA FILA - FILA VAZIA\n";
                sleep_for(0.25s);
				isPistaVazia = true;  
                sleep_for(0.25s);
                cout << endl << "\nFILA DE AVIOES ESPERANDO:\n";
			    cout << "SEM AVIOES ESPERANDO PARA POUSAR/DECOLAR\n";
                sleep_for(0.25s);
            }
		}
		else if(isPistaVazia && (!isVazia)){
			sleep_for(0.25s);
            cout << endl << "-------------PISTAS OCUPADAS--------------\n" << endl;
            sleep_for(0.25s);
            for(i = 1; i <= quantAvioes; i++)
            {
                imprimePistaDePouso(i, tipoNaPista[i-1], aviaoNaPista[i-1]);
            }
            quantAvioes = 0;
            isVazia = true;
		}
    	else if(isPistaVazia && isVazia){
		    sleep_for(0.25s);
            cout << endl << "TODOS OS AVIOES POUSARAM/DECOLARAM! Sem trafego aereo no momento\n";
            sleep_for(0.25s);
		}
        else
        {
            sleep_for(0.25s);
            cout << endl << "-------------PISTAS OCUPADAS--------------\n" << endl;
            sleep_for(0.25s);
            for(i = 1; i <= quantAvioes; i++)
            {
                imprimePistaDePouso(i, tipoNaPista[i-1], aviaoNaPista[i-1]);
            }
            quantAvioes = 0;
        }
        sleep_for(1.25s);
    }
}

void imprimePistaDePouso(int quant, char tipo, int idAviao)
{
    if(tipo == 'D')
    {
        cout << "PISTA " << quant << " sendo usada pelo aviao " << idAviao << " >>>" << endl;
    }

    if(tipo == 'P')
    {
        cout << "PISTA " << quant << " sendo usada pelo aviao " << idAviao << " <<<" << endl;
    }
    sleep_for(0.5s);   
}