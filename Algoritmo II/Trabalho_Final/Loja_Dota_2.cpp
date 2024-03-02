#include <iostream>
#include <conio.h>
#include <fstream>
#define MAX 100
using namespace std;

struct atributos
{
    int inteligencia;
    int agilidade;
    int forca;
    int hp;
    int mana;
    int armadura;
    int resistenciaMagica;
};

struct itens
{
    string nome;
    string descricao;

    int preco;
    int tag;
    int quantidade;

    atributos atributosItens;

    bool isConsumivel;
    bool isUsavel;
    bool isCombinado;
    int primeiro, segundo, terceiro;
};

struct loja
{
    itens itensLoja[MAX];
};

struct jogador
{
    atributos atributosBase;
    atributos atributosAtuais;

    int gold;

    itens inventario[5];
    itens estoque[2];
};

void criarItensNaLoja(loja*, int, string);
void menu(bool*,bool*,bool*);
void verInventarioJogador(jogador*, bool*, bool*);
int buscarItem();
int organizarItens();


int main()
{
    loja lojaSecreta, lojaBase;
    itens itensConbinados[MAX];
    jogador player;

    int totalItensBase = 5, totalItensSecretos = 1, totalItensCombinados = 0;
    string nomeArq1 = "LojaBase.txt", nomeArq2 = "LojaSecreta.txt", nomeArq3 = "Player.txt", nomeArq4 = "itensCombinados"; 
    bool isOn = true, isMenu = true, isInventario = false;
    
    criarItensNaLoja(&lojaBase,totalItensBase,nomeArq1);
    criarItensNaLoja(&lojaSecreta,totalItensSecretos,nomeArq2);
    
    while(isOn)
    {
       if(isMenu) menu(&isOn,&isMenu,&isInventario);
       if(isInventario) verInventarioJogador(&player, &isMenu, &isInventario);
    }
   
    return 0;
}

void criarItensNaLoja(loja *Loja, int totalItens, string arquivo)
{
    ifstream itens(arquivo);
    string chave;
    for(int i = 0; i < totalItens; i++)
    {
        string num = to_string(i+1);
        while(itens >> chave && chave != num)
        {
            if(chave == "Nome:")
            {
                getline(itens >> ws, Loja->itensLoja[i].nome);
            }
            if(chave == "Descricao:")
            {
                getline(itens >> ws, Loja->itensLoja[i].descricao);
            }
            if(chave == "Preco:")
            {
                itens >> Loja->itensLoja[i].preco;
            }
            if(chave == "Tag:")
            {
                itens >> Loja->itensLoja[i].tag;
            }
            if(chave == "Quantidade:")
            {
                itens >> Loja->itensLoja[i].quantidade;
            }
            if(chave == "Inteligencia:")
            {
                itens >> Loja->itensLoja[i].atributosItens.inteligencia;
            }
            if(chave == "Agilidade:")
            {
                itens >> Loja->itensLoja[i].atributosItens.agilidade;
            }
            if(chave == "Forca:")
            {
                itens >> Loja->itensLoja[i].atributosItens.forca;
            }
            if(chave == "HP:")
            {
                itens >> Loja->itensLoja[i].atributosItens.hp;
            }
            if(chave == "Mana:")
            {
                itens >> Loja->itensLoja[i].atributosItens.mana;
            }
            if(chave == "Armadura:")
            {
                itens >> Loja->itensLoja[i].atributosItens.armadura;
            }
            if(chave == "ResistenciaMagica:")
            {
                itens >> Loja->itensLoja[i].atributosItens.resistenciaMagica;
            }
            if(chave == "isConsumivel:")
            {
                itens >> Loja->itensLoja[i].isConsumivel;
            }
            if(chave == "isUsavel:")
            {
                itens >> Loja->itensLoja[i].isUsavel;
            }
        }
    }
    itens.close();
}

void menu(bool *isOn, bool *isMenu, bool *isInventario)
{
    cout << "Bem vindo ao DOTA 2 Lojas e Inventario Simulator!" << endl;
    cout << "1 - Comprar em umas das Lojas" << endl;
    cout << "2 - Verificar Itens da Loja" << endl;
    cout << "3 - Verificar Inventario" << endl;
    cout << "4 - Ganhar Gold" << endl;
    cout << "5 - Verificar Atributos" << endl;
    cout << "0 - Sair" << endl;
    if(_kbhit)
    {
        char botao = _getch();
        switch (botao)
        {
        case '1':
            system("cls");  
            cout << "Abre as opcoes para escolher a loja" << endl;
            break;
        case '2':
            system("cls");  
            cout << "Verifica quais itens estao na loja" << endl;
            break;
        case '3':
            system("cls");  
            *isMenu = false;
            *isInventario = true;
            break;
        case '4':
            system("cls");  
            cout << "Abre as opcoes para ganhar gold" << endl;
            break;
        case '5':
            system("cls");  
            cout << "Mostra os atributos" << endl;
            break;
        case '0':
            system("cls");  
            *isOn = false;
            break;
        default:
            system("cls");
            break;
        }
    }
}

void verInventarioJogador(jogador *player, bool *isMenu, bool *isInventario)
{
    cout << "Inventario do Jogador:" << endl;
    for(int i = 0; i < 6; i++)
    {
        if(player->inventario[i].nome.empty())
        {
            cout << "Sem itens no espaco " << i+1 << endl;
        } else {
            cout << player->inventario[i].nome;
        }
    }
    cout << "\n";
    cout << "Estoque do Jogador: " << endl;
    for(int i = 0; i < 3; i++)
    {
        if(player->estoque[i].nome.empty())
        {
            cout << "Sem itens no espaco " << i+1 << endl;
        } else {
            cout << player->estoque[i].nome;
        }
    }
    cout << "\n1 - Alterar itens entre estoque/inventario" << endl;
    cout << "2 - Ordenar estoque/inventario" << endl;
    cout << "3 - Voltar ao menu" << endl;

    if(_kbhit)
    {
        char botao = _getch();
        switch (botao)
        {
        case '1':
            system("cls");  
            cout << "Abre as opcoes para trocar itens" << endl;
            break;
        case '2':
            system("cls");  
            cout << "vai para a funcao de ordenacao" << endl;
            break;
        case '3':
            system("cls");  
            *isMenu = true;
            *isInventario = false;
            break;
        default:
            system("cls");
            break;
        }
    }
}