#include <iostream>
using namespace std;
#include "LDuplamente_Encadeada.h"

int main(void)
{
   	no *listaDePilotos, *podio;
	int ut, piloto, posicao, kmPercorridos, id, i, kmTotal = 500;
	int continua = 1;
	
    listaDePilotos = inicializa_Pilha(listaDePilotos);    	
    podio=inicializa_Pilha(podio);
    
	listaDePilotos = PUSH(listaDePilotos, 1, 0, 15);
	listaDePilotos = PUSH(listaDePilotos, 5, 0, 19);
	listaDePilotos = PUSH(listaDePilotos, 3, 0, 12);
	listaDePilotos = PUSH(listaDePilotos, 2, 0, 17);
	listaDePilotos = PUSH(listaDePilotos, 4, 0, 13);

	cout << "POSICAO INICIAL DA CORRIDA DE "<< kmTotal << " KMs!!" << endl;
	exibe(listaDePilotos);

	for(ut=1; ut<=5 ; ut++){
		
		cout << endl << "__________________________" << endl;
		cout << "----- CHECKPOINT: "<< ut << " -----" << endl;
	
		cout << "\nPLACAR DA CORRIDA:\n";
		exibe(listaDePilotos);
		cout << "\n";
		exibe(listaDePilotos);
		
	}
}
