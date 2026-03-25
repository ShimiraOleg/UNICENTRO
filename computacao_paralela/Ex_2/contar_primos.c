#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <omp.h>

#define N 1000
#define S 100

int count_primes_omp(int n)
{
    int nsqrt = (int)sqrt((double)n);
    char *is_prime_base = (char *)malloc((nsqrt + 2) * sizeof(char));
    
    memset(is_prime_base, 1, (nsqrt + 2) * sizeof(char));
    is_prime_base[0] = is_prime_base[1] = 0;
    for (int i = 2; i <= nsqrt; i++) {
        if (is_prime_base[i]) {
            for (int j = i * i; j <= nsqrt; j += i)
                is_prime_base[j] = 0;
        }
    }

    int  base_count = 0;
    
    for (int i = 2; i <= nsqrt; i++)
        if (is_prime_base[i]) base_count++;

    int *primes = (int *)malloc(base_count * sizeof(int));
    int  idx    = 0;

    for (int i = 2; i <= nsqrt; i++)
        if (is_prime_base[i]) primes[idx++] = i;

    free(is_prime_base);

    int total_blocks = (n / S) + 1;
    int result = 0;

    #pragma omp parallel
    {
        int ID          = omp_get_thread_num();
        int num_threads = omp_get_num_threads();
        int workload    = (total_blocks + num_threads - 1) / num_threads;
        int start_blk   = ID * workload;
        int end_blk     = start_blk + workload;
        char *block = (char *)malloc(S * sizeof(char));
        int local_count = 0;
        
        for (int k = start_blk; (k < end_blk) && (k * S <= n); k++) {
            memset(block, 1, S * sizeof(char));
            int start_val = k * S;
            for (int p = 0; p < base_count; p++) {
                int pr        = primes[p];
                int start_idx = (start_val + pr - 1) / pr;
                int j         = (start_idx > pr ? start_idx : pr) * pr - start_val;
                for (; j < S; j += pr)
                    block[j] = 0;
            }
            if (k == 0) {
                block[0] = 0;
                if (S > 1) block[1] = 0;
            }
            for (int i = 0; i < S && start_val + i <= n; i++)
                if (block[i]) 
                {
                    local_count++;
                    #pragma omp critical
                    {
                        printf("Thread %d - %d\n", ID, start_val + i);
                    }
                }
        }
        free(block);
        #pragma omp critical
        {
            result += local_count;
        }
    }
    free(primes);
    return result;
}

int main()
{
    double t_start = omp_get_wtime();
    int total = count_primes_omp(N);
    double t_end   = omp_get_wtime();

    printf("\nQuantidade de primos de 1 a %d: %d\n", N, total);
    return 0;
}