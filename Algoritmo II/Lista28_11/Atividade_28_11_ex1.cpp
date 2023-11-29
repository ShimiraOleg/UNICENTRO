#include <iostream>
#define T 5
using namespace std;

void minMax(int*, int*, int*);

int main()
{
    int vetor[T] = {8, 4, 7, 2, 10};
    int min, max;

    minMax(vetor, &min, &max);

    cout << "min = " << min << endl;
    cout << "max = " << max << endl;

    return 0;
}

void minMax(int *vetor, int *min, int *max)
{
    *min = *vetor;
    *max = *vetor;
    for(register int i = 0; i < T; i++)
    {
        if(*min >= *(vetor + i))
        {
            *min = *(vetor + i);
        }
        if(*max <= *(vetor + i))
        {
            *max = *(vetor + i);
        }
    }
}