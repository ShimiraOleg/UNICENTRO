#include <stdio.h>

#include <iostream>
using namespace std;

#include "LDuplamente_Encadeada.h"

int main(void)
{
   no *P, *F;
   int c,x;
 
   P = inicializa_Pilha(P);
   F = inicializa_Fila(F);
   do 
   {
      printf("\n------------------------------------\n");
      printf("PILHA - LISTA DUPLAMENTE ENCADEADA \n");
      printf("1 - PUSH - INSERE ITEM NA PILHA\n");
      printf("2 - POP - REMOVE ITEM DA PILHA\n");
      printf("3 - Imprime Itens da PILHA");
      printf("\n------------------------------------\n");
      printf("FILA - LISTA DUPLAMENTE ENCADEADA \n");
      printf("4 - INSERE ITEM NA FILA\n");
      printf("5 - REMOVE ITEM DA FILA\n");
      printf("6 - Imprime Itens da FILA\n");
      printf("7 - Imprime Itens da FILA na ordem Inversa");
      printf("\n------------------------------------\n");
      printf("8 - SAIR\n");
      printf("\n Escolha: ");

      cin >> c;

      switch (c) {
         case 1: 
			   printf(" \nEntre com o item a ser inserido na PILHA: ");
			   cin >> x;
			   P = PUSH(P,x);
            break;
         case 2:
			   x=-1; 
		      P = POP(P,&x);
		      if (x != -1)
				   cout << endl << " Item retirado da PILHA: " << x;
			   break;
		   case 3: 
            printf("\n");
  		      imprime_Pilha(P);
 			   break;
         case 4: 
			   // a ser desenvolvido pelo aluno
		      //printf(" \nEntre com o item a ser inserido na FILA: ");
			   //cin >> x;
			   //F = insere_Final_Fila(F,x);
            break;
         case 5: 
			   //x=-1; 
 		      //F = remove_Inicio_Fila(F,&x);
		      //if (x != -1)
				  // cout << endl << " Item retirado da FILA: " << x;
			   //break;
         case 6: 
            //printf("\n");
  		      // a ser desenvolvido
  		      //imprime_Fila(F);
 			break;
         case 7: 
            //printf("\n");
  		      // a ser desenvolvido
			   //imprime_Inverso_Fila(F);
 			break;
         case 8: 
		      exit(0);
            break;
      };
   } while (c != 8);
}
