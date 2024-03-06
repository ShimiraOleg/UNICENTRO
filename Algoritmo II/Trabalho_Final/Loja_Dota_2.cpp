#include <iostream>
#include <conio.h>
#include <fstream>
#include <cassert>
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

    atributos atributosItens;
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

    itens inventario[MAX];
};

void criarItensNaLoja(loja*, int, string);
void atribuirAtributos(jogador*, string);
void menu(loja*, loja*, loja*, jogador*, int, int, int*);
void verInventarioJogador(jogador*);
void verStatsPlayer(jogador);
void ganharGold(jogador*);
void comprarNaLoja(loja, jogador*, int);
void organizarItens(loja*, loja*, int, int);
void ordenar(loja*, int, int);
void adcionarAtributos(jogador*, itens);
void removerAtributos(jogador*, itens);
void printItem(itens);
void testeBuscaItemPorTagBase(loja);
int buscarItemPorTag(itens[], int, int);
loja escolherLoja(loja, loja, int, int, int*);

bool isOn = true, isMenu = true, isInventario = false, isPlayerMenu = false, isGoldMenu = false, isComprando = false, isOrdenar = false;

int main()
{
    loja lojaSecreta, lojaBase, lojaAtual;
    itens itens[MAX];
    jogador player;

    string nomeArq1 = "LojaBase.txt", nomeArq2 = "LojaSecreta.txt", nomeArq3 = "Player.txt";

    int totalItensBase = 7, totalItensSecretos = 4, totalItensAtual = 0; 
    
    criarItensNaLoja(&lojaBase,totalItensBase,nomeArq1);
    criarItensNaLoja(&lojaSecreta,totalItensSecretos,nomeArq2);
    atribuirAtributos(&player, nomeArq3);
    testeBuscaItemPorTagBase(lojaBase);
    cout << "Teste inicial funciona!\n" << endl;
    
    lojaAtual = lojaBase;

    while(isOn)
    {
       if(isMenu) menu(&lojaAtual, &lojaBase, &lojaSecreta, &player, totalItensBase, totalItensSecretos, &totalItensAtual);
       if(isInventario) verInventarioJogador(&player);
       if(isPlayerMenu) verStatsPlayer(player);
       if(isGoldMenu) ganharGold(&player);
       if(isComprando) comprarNaLoja(lojaAtual, &player, totalItensAtual);
       if(isOrdenar) organizarItens(&lojaBase, &lojaSecreta, totalItensBase, totalItensSecretos);
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
        }
    }
    itens.close();
}

void atribuirAtributos(jogador *Player, string arquivo)
{
    ifstream jogadorBase(arquivo);
    string chave;
    while(jogadorBase >> chave)
    {
        if(chave == "Inteligencia:")
        {
            jogadorBase >> Player->atributosBase.inteligencia;
        }
        if(chave == "Agilidade:")
        {
            jogadorBase >> Player->atributosBase.agilidade;
        }
        if(chave == "Forca:")
        {
            jogadorBase >> Player->atributosBase.forca;
        }
        if(chave == "HP:")
        {
            jogadorBase >> Player->atributosBase.hp;
        }
        if(chave == "Mana:")
        {
            jogadorBase >> Player->atributosBase.mana;
        }
        if(chave == "Armadura:")
        {
            jogadorBase >> Player->atributosBase.armadura;
        }
        if(chave == "ResistenciaMagica:")
        {
            jogadorBase >> Player->atributosBase.resistenciaMagica;
        }
        if(chave == "Gold:")
        {
            jogadorBase >> Player->gold;
        }
    }
    jogadorBase.close();

}

void menu(loja *atual, loja *base, loja *secreta, jogador *player, int totalBase, int totalSecreto, int *totalAtual)
{
    cout << "Bem vindo ao DOTA 2 Lojas e Inventario Simulator!" << endl;
    cout << "1 - Comprar em umas das Lojas" << endl;
    cout << "2 - Ordenar Lojas" << endl;
    cout << "3 - Verificar Inventario" << endl;
    cout << "4 - Ganhar Gold" << endl;
    cout << "5 - Verificar Atributos" << endl;
    cout << "0 - Sair" << endl;
    if(_kbhit)
    {
        char botao = _getch();
        switch (botao) {
        case '1':
            system("cls");  
            *atual = escolherLoja(*base, *secreta, totalBase, totalSecreto, totalAtual);
            if(atual->itensLoja[0].nome.empty())
            {
                system("cls");
                cout << "O valor inserido para a loja eh invalido\n" << endl;
            }
            else
            {
                isMenu = false;
                isComprando = true;
            }
            break;
        case '2':
            system("cls");  
            isMenu = false;
            isOrdenar = true;
            break;
        case '3':
            system("cls");  
            isMenu = false;
            isInventario = true;
            break;
        case '4':
            system("cls");  
            isMenu = false;
            isGoldMenu = true;
            break;
        case '5':
            system("cls");  
            isMenu = false;
            isPlayerMenu = true;
            break;
        case '0':
            system("cls");  
            isOn = false;
            break;
        default:
            system("cls");
            break;
        }
    }
}

void verInventarioJogador(jogador *player)
{
    int item;
    cout << "Inventario do Jogador:" << endl;
    for(int i = 0; i < 6; i++)
    {
        if(player->inventario[i].nome.empty())
        {
            cout << "Sem itens no espaco " << i+1 << endl;
        } else {
            cout << player->inventario[i].nome << "(" << player->inventario[i].tag << ")" << endl;
        }
    }
    cout << "\n";

    cout << "\n1 - Verificar itens" << endl;
    cout << "2 - Apagar item do inventario" << endl;
    cout << "0 - Voltar ao menu" << endl;

    if(_kbhit)
    {
        char botao = _getch();
        switch (botao)
        {
        case '1':  
            cout << "\nEscolha um dos itens acima pela tag (numero entre parentesis)" << endl;
            cin >> item;
            item = buscarItemPorTag(player->inventario, item, 5);
            if(item == -1)
            {
                system("cls");
                cout << "Opcao invalida!" << endl;
            }
            else
            {
                system("cls");
                printItem(player->inventario[item]);
            }
            break;
        case '2':
            cout << "\nEscolha um dos itens acima pela tag (numero entre parentesis)" << endl;
            cin >> item;
            item = buscarItemPorTag(player->inventario, item, 5);
            if(item == -1 || cin.fail())
            {
                system("cls");
                cout << "Opcao invalida!" << endl;
            }
            else
            {
                system("cls");
                removerAtributos(player, player->inventario[item]);
                player->inventario[item] = player->inventario[6];
            }
            break;
        case '0':
            system("cls");  
            isMenu = true;
            isInventario = false;
            break;
        default:
            system("cls");
            break;
        }
    }
}

void verStatsPlayer(jogador player)
{
    cout << "Stats do jogador:\n" << endl;
    cout << "Inteligencia: " << player.atributosBase.inteligencia + player.atributosAtuais.inteligencia << endl;
    cout << "Agilidade: " << player.atributosBase.agilidade + player.atributosAtuais.agilidade << endl;
    cout << "Forca: " << player.atributosBase.forca + player.atributosAtuais.forca << endl;
    cout << "\nHP: " << player.atributosBase.hp + player.atributosAtuais.hp << endl;
    cout << "Mana: " << player.atributosBase.mana + player.atributosAtuais.mana << endl;
    cout << "\nArmadura: " << player.atributosBase.armadura + player.atributosAtuais.armadura << endl;
    cout << "Resistencia Magica: " << player.atributosBase.resistenciaMagica + player.atributosAtuais.resistenciaMagica << endl;
    cout << "\naperte '0' para voltar ao menu";
    if(_kbhit)
    {
        char botao = _getch();
        switch (botao){
        case '0':
            system("cls");  
            isPlayerMenu = false;
            isMenu = true;
            break;
        
        default:
            system("cls");  
            break;
        }
    }
}

void ganharGold(jogador *player)
{
    cout << "Voce tem " << player->gold << " de gold" << endl;
    cout << "1 - farm (adciona 10 de gold)" << endl;
    cout << "2 - kill (adciona 100 de gold)" << endl;
    cout << "3 - megakill (adciona 1000 de gold)" << endl;
    cout << "4 - Rampage (adciona 10000 de gold)" << endl;
    cout << "0 - voltar ao menu" << endl;
    if(_kbhit)
    {
        char botao = _getch();
        switch (botao){
        case '1':
            system("cls");  
            player->gold += 10;
            break;
        case '2':
            system("cls");  
            player->gold += 100;
            break;
        case '3':
            system("cls");  
            player->gold += 1000;
            break;
        case '4':
            system("cls");  
            player->gold += 10000;
            break;
        case '0':
            system("cls");  
            isGoldMenu = false;
            isMenu = true;
            break;
        
        default:
            system("cls");  
            break;
        }
    }

}

loja escolherLoja(loja base, loja secreta, int totalBase, int totalSecreto, int *totalAtual)
{
    loja *lojaPtr;
    lojaPtr = new loja;
    cout << "Escolha uma loja:" << endl;
    cout << "1 - Loja Base" << endl;
    cout << "2 - Loja Secreta" << endl;
    if(_kbhit)
    {
        char botao = _getch();
        switch (botao)
        {
        case '1':
            system("cls");
            *lojaPtr = base;
            *totalAtual = totalBase;
            return *lojaPtr;
            delete lojaPtr;
            break;
        case '2':
            system("cls");
            *lojaPtr = secreta;
            *totalAtual = totalSecreto;
            return *lojaPtr;
            delete lojaPtr;
            break;
        default:
            system("cls");
            break;
        }
    }
}

void comprarNaLoja(loja atual, jogador *player, int totalAtual)
{
    int compra;
    for(int i = 0; i < totalAtual; i++)
    {
        cout << i+1 << " - " << atual.itensLoja[i].nome << " : " << atual.itensLoja[i].preco << " de gold" << endl;
    }
    cout << "Voce tem: " << player->gold << " de gold" << endl;
    cout << "\nEscolha qual dos itens voce vai comprar (Digite '0' para comprar nenhum)" << endl;
    cin >> compra;

    if(compra == 0)
    {
        system("cls");  
        isComprando = false;
        isMenu = true;
        return;        
    }
    compra--;
    for(int i = 0; i < 6; i++)
    {
        if(player->inventario[i].nome == atual.itensLoja[compra].nome)
        {
            system("cls");  
            cout << "Voce ja tem esse item" << endl;
            break;
        }
        else if(player->gold < atual.itensLoja[compra].preco)
        {
            system("cls");  
            cout << "Voce nao tem gold o bastante para comprar esse item" << endl;
            break;            
        }
        else if(player->inventario[i].nome.empty())
        {
            system("cls");
            player->inventario[i] = atual.itensLoja[compra];
            player->gold -= atual.itensLoja[compra].preco;
            adcionarAtributos(player, atual.itensLoja[compra]);
            isComprando = false;
            isMenu = true;
            break;
        }
        else
        {
            system("cls");
            cout << "Seu inventario esta cheio!\n" << endl;
        }

    }
}

void organizarItens(loja *base, loja *secreta, int tamanhoBase, int tamanhoSecreto)
{
    int forma;
    cout << "Escolha como ordenar as lojas:\n" << endl;
    cout << "1 - Maior Preco" << endl;
    cout << "2 - Ordem Alfabetica" << endl;
    cout << "3 - Ordem Original" << endl;
    if(_kbhit)
    {
        forma = _getch();
        switch (forma)
        {
        case '1':
            system("cls"); 
            ordenar(base, forma, tamanhoBase);
            ordenar(secreta, forma, tamanhoSecreto);
            isOrdenar = false;
            isMenu = true;
        case '2':
            system("cls"); 
            ordenar(base, forma, tamanhoBase);
            ordenar(secreta, forma, tamanhoSecreto);
            isOrdenar = false;
            isMenu = true;
        case '3':
            system("cls"); 
            ordenar(base, forma, tamanhoBase);
            ordenar(secreta, forma, tamanhoSecreto);
            isOrdenar = false;
            isMenu = true;
        default:
            system("cls");
            break;
        }
    }
}

void ordenar(loja *atual, int forma, int tamanho)
{ 
    if (tamanho == 1) return;

    for (int i = 0; i <= tamanho - 2; i++) {
        if(forma == 49)
        {
            if (atual->itensLoja[i].preco < atual->itensLoja[i+1].preco) 
            {
                itens temp = atual->itensLoja[i+1];
                atual->itensLoja[i+1] = atual->itensLoja[i];
                atual->itensLoja[i] = temp;
            }
        }
        if(forma == 50)
        {
            if (atual->itensLoja[i].nome > atual->itensLoja[i+1].nome) 
            {
                itens temp = atual->itensLoja[i+1];
                atual->itensLoja[i+1] = atual->itensLoja[i];
                atual->itensLoja[i] = temp;
            }
        }
        if(forma == 51)
        {
            if (atual->itensLoja[i].tag > atual->itensLoja[i+1].tag) 
            {
                itens temp = atual->itensLoja[i+1];
                atual->itensLoja[i+1] = atual->itensLoja[i];
                atual->itensLoja[i] = temp;
            }
        }
    }
    ordenar(atual, forma, tamanho - 1);
}

void adcionarAtributos(jogador *player, itens valor)
{
    player->atributosAtuais.agilidade += valor.atributosItens.agilidade;
    player->atributosAtuais.inteligencia += valor.atributosItens.inteligencia;
    player->atributosAtuais.forca += valor.atributosItens.forca;
    player->atributosAtuais.hp += valor.atributosItens.hp;
    player->atributosAtuais.mana += valor.atributosItens.mana;
    player->atributosAtuais.armadura += valor.atributosItens.armadura;
    player->atributosAtuais.resistenciaMagica += valor.atributosItens.resistenciaMagica;
}

void removerAtributos(jogador *player, itens valor)
{
    player->atributosAtuais.agilidade -= valor.atributosItens.agilidade;
    player->atributosAtuais.inteligencia -= valor.atributosItens.inteligencia;
    player->atributosAtuais.forca -= valor.atributosItens.forca;
    player->atributosAtuais.hp -= valor.atributosItens.hp;
    player->atributosAtuais.mana -= valor.atributosItens.mana;
    player->atributosAtuais.armadura -= valor.atributosItens.armadura;
    player->atributosAtuais.resistenciaMagica -= valor.atributosItens.resistenciaMagica;
}

void printItem(itens item)
{
    system("cls");
    if(!(item.nome.empty())) cout << "Nome: " << item.nome << endl;
    if(!(item.descricao.empty())) cout << "Descricao: " << item.descricao << endl;
    if(item.atributosItens.inteligencia != 0) cout << "Inteligencia: " << item.atributosItens.inteligencia << endl;
    if(item.atributosItens.agilidade != 0) cout << "Agilidade: " << item.atributosItens.agilidade << endl;
    if(item.atributosItens.forca != 0) cout << "Forca: " << item.atributosItens.forca << endl;
    if(item.atributosItens.hp != 0) cout << "HP: " << item.atributosItens.hp << endl;
    if(item.atributosItens.mana != 0) cout << "Mana: " << item.atributosItens.mana << endl;
    if(item.atributosItens.armadura != 0) cout << "Armadura: " << item.atributosItens.armadura << endl;
    if(item.atributosItens.resistenciaMagica != 0) cout << "Resistencia Magica: " << item.atributosItens.resistenciaMagica << endl;
    cout << "\n";
}

int buscarItemPorTag(itens item[MAX], int busca, int tamanho)
{
    int i;
    for(i = 0; i < tamanho; i++)
    {
        if(item[i].tag == busca)
        {
            return i;
        }
    }
    return -1;
}

void testeBuscaItemPorTagBase(loja base)
{
    assert(buscarItemPorTag(base.itensLoja, 5, 6) == 5);
    assert(buscarItemPorTag(base.itensLoja, 4, 6) == 4);
    assert(buscarItemPorTag(base.itensLoja, 100, 6) == -1);
}