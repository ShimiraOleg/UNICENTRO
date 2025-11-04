/*
Grupo: Quinaiers
Alunos: André Cidade Irie, Guilherme Licori, Mateus de Oliveira Lopes
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <limits>
#include <queue>
#include <algorithm>

using namespace std;

const double INF = numeric_limits<double>::infinity();
const double EPS = 1e-9;

struct Ponto {
    double x, y;
    Ponto(double x = 0, double y = 0) : x(x), y(y) {}

    Ponto operator+(const Ponto& other) const {
        return Ponto(x + other.x, y + other.y);
    }
    Ponto operator-(const Ponto& other) const {
        return Ponto(x - other.x, y - other.y);
    }
    Ponto operator*(double k) const {
        return Ponto(x * k, y * k);
    }
};

struct Segmento {
    Ponto p1, p2;
    Segmento(Ponto p1 = Ponto(), Ponto p2 = Ponto()) : p1(p1), p2(p2) {}
};

double interno(Ponto p1, Ponto p2) {
    return p1.x * p2.x + p1.y * p2.y;
}

double cruzamento(Ponto p1, Ponto p2) {
    return p1.x * p2.y - p1.y * p2.x;
}

double distancia(Ponto p1, Ponto p2) {
    return hypot(p1.x - p2.x, p1.y - p2.y);
}

bool ehColinear(Ponto p, Ponto q, Ponto r) {
    return fabs(cruzamento(p - q, r - q)) < EPS;
}

bool ehInterligado(Ponto p, Ponto q, Ponto r) {
    return ehColinear(p, q, r) && interno(p - q, r - q) < EPS;
}

Ponto segmentoMaisPertoDaLinha(Ponto p, Ponto a, Ponto b) {
    if (fabs(a.x - b.x) < EPS && fabs(a.y - b.y) < EPS) {
        return a;
    }

    double denom = interno(b - a, b - a);
    if (fabs(denom) < EPS) {
        return a;
    }

    double u = interno(p - a, b - a) / denom;
    if (u < 0.0) {
        return a;
    }
    if (u > 1.0) {
        return b;
    }
    return a + (b - a) * u;
}

double distanciaAteSegmento(Ponto p, Ponto a, Ponto b) {
    Ponto c = segmentoMaisPertoDaLinha(p, a, b);
    return distancia(p, c);
}

bool segmentoEhIntersectado(Ponto a, Ponto b, Ponto p, Ponto q) {
    Ponto u = b - a;
    Ponto v = q - p;
    if (fabs(cruzamento(v, u)) < EPS) {
        return ehInterligado(a, p, b) || ehInterligado(a, q, b) ||
               ehInterligado(p, a, q) || ehInterligado(p, b, q);
    }

    double denom = cruzamento(u, v);
    double t = cruzamento(p - a, v) / denom;
    double s = cruzamento(p - a, u) / denom;

    return t >= 0.0 - EPS && t <= 1.0 + EPS && s >= 0.0 - EPS && s <= 1.0 + EPS;
}

double calcularDistancia(Segmento s1, Segmento s2) {
    if (segmentoEhIntersectado(s1.p1, s1.p2, s2.p1, s2.p2)) {
        return 0.0;
    }
    double u = min(distanciaAteSegmento(s1.p1, s2.p1, s2.p2),
                   distanciaAteSegmento(s1.p2, s2.p1, s2.p2));
    double v = min(distanciaAteSegmento(s2.p1, s1.p1, s1.p2),
                   distanciaAteSegmento(s2.p2, s1.p1, s1.p2));
    return min(u, v);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    while (cin >> N && N != 0) {
        vector<Segmento> segmentos;
        for (int i = 0; i < N; ++i) {
            int x, y, direcao;
            cin >> x >> y >> direcao;
            Ponto p1(x, y);
            Ponto p2;
            if (direcao < 0) {
                p2 = Ponto(x, y - direcao);
            } else {
                p2 = Ponto(x + direcao, y);
            }
            segmentos.push_back(Segmento(p1, p2));
        }

        vector<vector<double>> distancias(N, vector<double>(N, 0.0));
        vector<double> valor(N, INF);
        vector<bool> utilizado(N, false);

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < i; ++j) {
                distancias[i][j] = distancias[j][i] = calcularDistancia(segmentos[i], segmentos[j]);
            }
        }

        priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> filaDePrioridade;

        filaDePrioridade.push({0.0, 0});
        valor[0] = 0.0;

        while (!filaDePrioridade.empty()) {
            double d = filaDePrioridade.top().first;
            int index = filaDePrioridade.top().second;
            filaDePrioridade.pop();

            if (utilizado[index]) {
                continue;
            }
            if (index == 1) {
                break;
            }

            utilizado[index] = true;

            for (int i = 0; i < N; ++i) {
                if (!utilizado[i]) {
                    double distanciaNova = max(d, distancias[index][i]);
                    if (distanciaNova < valor[i]) {
                        valor[i] = distanciaNova;
                        filaDePrioridade.push({valor[i], i});
                    }
                }
            }
        }
        cout << fixed << setprecision(2) << valor[1] << "\n";
    }
    return 0;
}