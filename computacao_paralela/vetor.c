#include <stdio.h>
#include <omp.h>
#define tamanho 80

int main()
{
    int a[tamanho], resultado = 0, resultado_local[12], num_threads;
    for(int i = 0; i < tamanho; i++)
    {
        a[i] = i;
    }
    #pragma omp parallel
    {
        int ID = omp_get_thread_num();
        int resultado_temp = 0;
        num_threads = omp_get_num_threads();
        int workload = (tamanho + num_threads - 1) / num_threads;
        int start = ID * workload;
        int end = start + workload;

        for(int i = start; (i < end) && (i < tamanho); i++)
        {
            //resultado += a[i]; corrida crítica/depende da ordem
            resultado_temp += a[i];
            //printf("Resultado[%d] = %d\n",ID,resultado_local[ID]); 
        }
        resultado_local[ID] = resultado_temp;
    }
    for(int i = 0; i <= num_threads; i++)
    {
        resultado += resultado_local[i];
    }
    printf("Resultado = %d\n",resultado); 
}