#include <iostream>
#include <fstream>
#define MAX 100
using namespace std;

struct itens
{
    string nome;
    string descricao;

    int preco;
    int tag;

    int inteligencia;
    int agilidade;
    int forca;
    int hp;

    bool isConsumivel;
    bool isUsavel;
};

struct loja
{
    itens itensLoja[MAX];
};

int criarItensNasLojas();
int verificarJuncao();
int buscarItem();
int organizarItens();


int main()
{
    loja lojaSecreta, lojaNormal;
    int totalItens = 1, itemAtual;

    return 0;
}