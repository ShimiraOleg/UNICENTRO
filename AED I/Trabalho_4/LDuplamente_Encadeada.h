/*
 * LISTA DUPLAMENTE ENCADEADA
 */

/* Define o tipo de dado no */
struct no {
	int posicao;
	int id;
	int kmPercorridos;
	no *prev;
	no *prox;
};

no *inicializa_Pilha(no *L) {
	L = NULL;
	return L;
}

no *PUSH(no *L, int pos, int km, int id) {
	no *N;

	N = new no;
	N->kmPercorridos = km;
	N->posicao = pos;
	N->id = id;

	N->prev = NULL;
	N->prox = L;
	if (L != NULL)
		L->prev = N;
	L = N;
	return L;
}

no *POP(no *L, int *pos, int *km, int *id) {
	no *AUX;

	if (L != NULL) {
		*pos = L->posicao;
		*km = L->kmPercorridos;
		*id = L->posicao;
		AUX = L;
		L = L->prox;
		if (L != NULL)
			L->prev = NULL;
		delete AUX;
	}
	return L;
}

void exibe(no *L)
{
    no *P = L;
    while (P != NULL) {
		cout << "| PILOTO: " << P->id << "| POSICAO: " << P->posicao << "| KMs PERCORRIDOS: " << P->kmPercorridos << "|\n" ;
        P = P->prox;
    }
}

int verificaSeVazia(no *L) {
	if (L == NULL)
		return 1;
	else
		return 0;
}

no *addKM(no *L, int km, int id)
{
	no* N;
	N = L;
	if(!(verificaSeVazia(N)))
	{
		for(N; N->prox != NULL; N = N->prox)
		{
			if(N->id == id)
				N->kmPercorridos = km;

			if (N != NULL)
				N->prev = N;
		}
	}
	L = N;
	return L;
}