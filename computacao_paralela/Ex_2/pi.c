#include <stdio.h>
#include <omp.h>
#define tamanho 100000

int main() {
    double largura_passo = 1.0 / (double) tamanho, resultado = 0.0, resultado_local[12];
    int num_threads;

    #pragma omp parallel
    {
        int ID = omp_get_thread_num();
        double x, resultado_temp = 0.0;
        num_threads = omp_get_num_threads();
        int workload = (tamanho + num_threads - 1) / num_threads;
        int start = ID * workload;
        int end = start + workload;

        for (int i = start; (i < end) && (i < tamanho); i++) {
            x = (i + 0.5) * largura_passo;
            resultado_temp += 4.0 / (1.0 + x * x);
        }

        resultado_local[ID] = resultado_temp;
    }

    for (int i = 0; i < num_threads; i++) {
        resultado += resultado_local[i];
    }
    double pi = resultado * largura_passo;

    printf("Valor aproximado de Pi: %.15f\n", pi);
    return 0;
}