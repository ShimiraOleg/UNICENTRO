/*
Grupo: Quinaiers
Alunos: André Cidade Irie, Guilherme Licori, Mateus de Oliveira Lopes
*/

#include <bits/stdc++.h>
using namespace std;

#define MAXN 10005

struct Aresta {
    int u, v;           
    long long custo;
    
    Aresta(int _u, int _v, long long _custo) {
        u = _u;
        v = _v;
        custo = _custo;
    }
    
    bool operator<(const Aresta& outra) const {
        return custo < outra.custo;
    }
};

class UnionFind {
private:
    int pai[MAXN];      
    int ranking[MAXN]; 
    int numConjuntos;   
    
public:
    void inicializar(int n) {
        numConjuntos = n;
        for (int i = 1; i <= n; i++) {
            pai[i] = i;      
            ranking[i] = 0;  
        }
    }
    int encontrar(int x) {
        if (pai[x] != x) {
            pai[x] = encontrar(pai[x]);
        }
        return pai[x];
    }
    bool unir(int x, int y) {
        int raizX = encontrar(x);
        int raizY = encontrar(y);
        
        if (raizX == raizY) {
            return false;
        }
        
        if (ranking[raizX] < ranking[raizY]) {
            pai[raizX] = raizY;
        } else if (ranking[raizX] > ranking[raizY]) {
            pai[raizY] = raizX;
        } else {
            pai[raizY] = raizX;
            ranking[raizX]++;
        }
        
        numConjuntos--;
        return true;
    }
    
    int obterNumeroConjuntos() {
        return numConjuntos;
    }
};

int N;
vector<Aresta> arestas; 
UnionFind uf;

int main() {
        
    scanf("%d", &N);
    uf.inicializar(N);
        
    for (int i = 1; i <= N - 1; i++) {
        int k;
        scanf("%d", &k);
            
        for (int idx = 0; idx < k; idx++) {
            int j;
            long long custo;
            scanf("%d %lld", &j, &custo);
                
            arestas.push_back(Aresta(i, j, custo));
        }
    }
    sort(arestas.begin(), arestas.end());
        
    long long custoTotal = 0;
    for (int i = 0; i < arestas.size(); i++) {
        int u = arestas[i].u;
        int v = arestas[i].v;
        long long custo = arestas[i].custo;

        if (uf.unir(u, v)) {
            custoTotal += custo;
        }
    }
    int numFamilias = uf.obterNumeroConjuntos();
        
    printf("%d %lld\n", numFamilias, custoTotal);
    
    return 0;
}