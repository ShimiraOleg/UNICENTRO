/*
 * LISTA DUPLAMENTE ENCADEADA
 */

/* Define o tipo de dado no */
struct no {
	int info;
	no *prev;
	no *prox;
};

/***** PILHA *****/
no *inicializa_Pilha(no *L) {
	L = NULL;
	return L;
}

no *PUSH(no *L, int x) {
	no *N;

	N = new no;
	N->info = x;

	N->prev = NULL;
	N->prox = L;
	if (L != NULL)
		L->prev = N;
	L = N;
	return L;
}

no *POP(no *L, int *n) {
	no *AUX;

	if (L != NULL) {
		*n = L->info;
		AUX = L;
		L = L->prox;
		if (L != NULL)
			L->prev = NULL;
		delete AUX;
	}
	return L;
}

void imprime_Pilha(no *L) {
	no *P;
	P = L;
	
	printf("\n Itens da Pilha (lista LIFO):");	
	while(P != NULL) {
		cout << endl <<  P->info;	
		P = P->prox;
	}
	printf("\n");
}

/***** FILA *****/

no *inicializa_Fila(no *L) {
	L = NULL;
	return L;
}

no *insere_Final_Fila(no *L, int x) {
	no *AUX, *ANT;
	AUX = new no;
	if(L == NULL)
	{
		AUX->prev = NULL;
		AUX->prox = L;
	}
	else
	{
		AUX = L;
		while(AUX->prox != NULL)
		{
			ANT->prox = AUX;
			AUX = AUX->prox;

		}
	}
	return L;
}

no *remove_Inicio_Fila(no *L, int *n) {
	no *AUX;

	if (L != NULL) {
		*n = L->info;
		AUX = L;
		L = L->prox;
		if (L != NULL)
			L->prev = NULL;
		free(AUX);
	}
	return L;
}

/*
// a ser desenvolvido
void imprime_Fila(no *L) {
	
}
*/

/*
// a ser desenvolvido 
void imprime_Inverso_Fila(no *L) {
	
} 
*/
