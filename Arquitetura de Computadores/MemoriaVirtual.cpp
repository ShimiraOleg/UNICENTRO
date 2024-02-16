#include <iostream>
#define MAX 100
using namespace std;

struct Page{
    int enderecoVirtual;
    int enderecoFisico;
    bool isDisco;
};

void criarPaginas(Page*, int*);
void criarRAM(int*, int, int*);
void criarDisco(int*, int, int*);
int buscarMV(int,Page*,int*,int*,int,int*,int*,int*);
void resultadosBMV(int,int,int*,int*);

int main()
{
    Page pagina[MAX];
    int memoriaRAM[MAX];
    int memoriaDisco[MAX];
    int tamanhoPagina = 80;
    int tamanhoMemoriaRAM = 4;
    int tamanhoMemoriaDisco = 40;
    int paginaUsada = 0;
    int RAMUsada = 0;
    int discoUsado = 0;
    int pageHit = 0;
    int pageMiss = 0;
    int endereco, resultadoBusca;

    criarPaginas(pagina,&paginaUsada);
    criarRAM(memoriaRAM,tamanhoMemoriaRAM,&RAMUsada);
    criarDisco(memoriaDisco,tamanhoMemoriaDisco,&discoUsado);

    cout << "Iniciando testes de busca de memoria virtual: \n" << endl;
    
    endereco = 42;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);
    
    endereco = 75;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);
    
    endereco = 17;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);
    
    endereco = 12;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);

    endereco = 13;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);

    endereco = 10;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);

    endereco = 42;
    resultadoBusca = buscarMV(endereco,pagina,memoriaRAM,memoriaDisco,tamanhoMemoriaRAM,&paginaUsada,&RAMUsada,&discoUsado);
    resultadosBMV(resultadoBusca, endereco, &pageMiss, &pageHit);

    cout << "Page Hit(s): " << pageHit << endl << "Page Miss(es): " << pageMiss << endl; 
}

void criarPaginas(Page *p, int *n)
{
    (p+0)->enderecoVirtual = 42;
    (p+0)->enderecoFisico = 0;
    (p+0)->isDisco = false;
    *n = *n + 1;

    (p+1)->enderecoVirtual = 75;
    (p+1)->enderecoFisico = 1;
    (p+1)->isDisco = false;
    *n = *n + 1;

    (p+2)->enderecoVirtual = 17;
    (p+2)->enderecoFisico = 12;
    (p+2)->isDisco = true;
    *n = *n + 1;

    (p+3)->enderecoVirtual = 12;
    (p+3)->enderecoFisico = 8;
    (p+3)->isDisco = true;
    *n = *n + 1;

    (p+4)->enderecoVirtual = 10;
    (p+4)->enderecoFisico = 3;
    (p+4)->isDisco = false;
    *n = *n + 1;

}

void criarRAM(int *p, int n, int *m)
{
    for(int i = 0; i < (n - 1); i++)
    {
        p[i] = 2 * (i+1);
        *m = *m + 1;
    }
}

void criarDisco(int *p, int n, int *m)
{
    for(int i = 0; i < (n - 1); i++)
    {
        p[i] = (2 * (i+1))-1;
        *m = *m + 1;
    }
}

int buscarMV(int end,Page *p, int *r, int *d, int tR, int *pU, int *rU, int *dU)
{
    for(int i = 0; i < *pU; i++)                        //Para todos os valores de paginas usados
    {
        if((p+i)->enderecoVirtual == end)               //Verifica se o endereço está em uma delas, se estiver:
        {
            if((p+i)->isDisco == false)                 //Se não está no Disco está em RAM
            {
                cout << "Valor esta na RAM" << endl;
                return r[(p+i)->enderecoFisico];        //Retorna o valor salvo no endereço em RAM
            }
            else if((p+i)->isDisco == true)             //Se está em Disco
            {
                cout << "Valor esta no Disco" << endl;
                if(tR > *rU)                            //Verifica se a RAM tem espaço, se tiver:
                {
                    cout << "RAM tem espaco. Inserindo o valor no disco para o espaco livre na RAM" << endl;
                    r[*rU] = d[(p+i)->enderecoFisico];  //transferencia de disco pra RAM no espaço disponivel
                    d[(p+i)->enderecoFisico] = 0;       //Anula o valor em disco pós transferência (melhor maneira que consegui representar)
                    (p+i)->enderecoFisico = *rU;        //Atualiza a pagina
                    *rU = *rU + 1;   
                    return r[(p+i)->enderecoFisico];    //Retorna o valor salvo no endereço em RAM
                }
                else
                {
                    cout << "RAM nao tem espaco. Substituindo um valor na RAM pelo valor no disco" << endl;
                    //Aqui seria usada uma política de substituição, cujo qual demoraria muito para programar
                    //Portanto, vou só substituir no primeiro endereço do vetor
                    r[0] = d[(p+i)->enderecoFisico];    //transferencia de disco pra RAM
                    d[(p+i)->enderecoFisico] = 0;       //Anula o valor em disco pós transferência (melhor maneira que consegui representar)
                    *dU = *dU - 1;
                    (p+i)->enderecoFisico = 0;          //Atualiza a pagina
                    return r[(p+i)->enderecoFisico];    //Retorna o valor salvo no endereço em RAM
                }
            }
        }
    }
    return -1;
}

void resultadosBMV(int rB, int end, int *pM, int *pH)
{
    if(rB == -1)
    {
        *pM = *pM + 1;
        cout << "O valor do endereco virtual " << end << " nao esta na pagina (Page Miss)" << endl;
        cout << "\n";
    }
    else
    {
        *pH = *pH + 1;
        cout << "o valor no endereco virtual "<< end << " eh: " << rB << " (Page Hit)" << endl;
        cout << "\n";
     }
}
