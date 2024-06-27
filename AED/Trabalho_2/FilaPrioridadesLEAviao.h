#include <chrono>
#include <thread>
using namespace std::this_thread;
using namespace std::chrono_literals;

struct node {
    int info;
    int prior;
    char tipo;
    node *link;
};

node *inicializaFP(node *L)
{
    L = NULL;
    return L;
}

node *insereFP(node *L, int valor, char tipo, int prior) 
{
    node *N, *P, *ANT;

    N = new node;
    N->info = valor;
    N->prior = prior;
    N->tipo = tipo;

    if (L == NULL) {
        L = N;
        N->link = NULL;
    }
    else {
        P = L;

        while ((P != NULL) && (prior >= P->prior)) {
            ANT = P;
            P = P->link;
        }
        if (P == L) {
            N->link = L;
            L = N;
        }
        else {
            ANT->link = N;
            N->link = P;
        }
    }
    return L;
}

node *removeFP(node *L, int *n, char *tipo, int *prior) {
	node *AUX;

	if (L != NULL) {
		*n = L->info;
		*prior = L->prior;
        *tipo = L->tipo; 
		AUX = L;
		L = L->link;
		delete AUX;
	}
	return L;
}

int verificaSeVazia(node *L) {
	if (L == NULL)
		return 1;
	else
		return 0;
}

void exibe(node *L)
{
    node *P = L;
    while (P != NULL) {
		cout << "|AVIAO: " << P->info << " |PRIORIDADE: " << P->prior << " |REQUISITA: " << P->tipo << "|\n" ;
        P = P->link;
        sleep_for(0.025s);
    }
}

node* insereFilaChegada(node *L, int data, char tipo ,int prior) {
	node *P, *N;

	N = (node *) malloc (sizeof(node)); 
	N->info = data; 
	N->prior = prior;
    N->tipo = tipo; 
	N->link = NULL; 
	 
	if (L == NULL){ 
		L = N;
	}
	else { 
		P = L;	
	
		while(P->link != NULL) {
			P = P->link;
		}
		P->link = N;
	} 
	return L;
}