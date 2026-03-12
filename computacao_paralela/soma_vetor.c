#include <stdio.h>
#include <omp.h>
#define tamanho 120

int main()
{
    int a[tamanho], b[tamanho], c[tamanho];
    for(int i = 0; i < tamanho; i++)
    {
        a[i] = i;
        b[i] = 2*i;
    }
    #pragma omp parallel
    {
        int ID = omp_get_thread_num();
        int num_threads = omp_get_num_threads();
        int workload = (tamanho + num_threads - 1) / num_threads;
        int start = ID * workload;
        int end = start + workload;

        for(int i = start; (i < end) && (i < tamanho); i++)
        {
            c[i] = a[i] + b[i];
        }
    }
    for(int i = 0; i < tamanho; i++){
        printf("c[%d] = %d\n",i,c[i]);
    }   
}