#include <stdio.h>
#include <math.h>
#define limit 1000
int* primes; // = { null, null, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1 ... };

void prime() { // 
	unsigned long long int i, j;
	int z = 1;
	primes = (int*)malloc(sizeof(int) * limit);

	for (i = 2; i < limit; i++) {
		primes[i] = 1;
	}


	for (i = 2; i < limit; i++) {
		if (primes[i]) {
			for (j = i; i * j < limit; j++) {
				primes[i * j] = 0;
			}
		}
	}
}


int main() {

	prime();

	int n;
	scanf("%d", &n);
	for (int i = 2; i < limit; i++) {
		if (primes[i]) {
			while (n % i == 0) {
				printf("%d\n", i);
				n /= i;
			}
		}
		else {
			continue;
		}
	}


	return 0;
}