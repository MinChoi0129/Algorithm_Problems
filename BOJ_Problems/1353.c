#include <stdio.h>
#include <math.h>

const double e = 2.7182818459045;

int solution()
{
    int S, P;
    scanf("%d %d", &S, &P);
    if (S == P)
        return 1;

    if (pow(e, S / e) < P)
        return -1;

    long double prv = -1;
    for (int i = 2;; i++)
    {
        long double cur = pow(1.l * S / i, i);
        if (prv > cur)
            return -1;
        if (cur >= P)
            return i;
        prv = cur;
    }
}

int main()
{
    printf("%d\n", solution());
    return 0;
}