#include <stdio.h>

int only_prime[10000] = { 0 };

int is_prime(int num) {
	if (num == 1) {
		return 0;
	}
	else if (num == 2) {
		return 1;
	}
	else {
		for (int i = 2; i <= num - 1; i++) {
			if (num % i == 0) {
				return 0;
			}
		}
		return 1;
	}
}

int main() {

	int m, n;
	int prime_count = 0;
	
	scanf("%d", &m);
	scanf("%d", &n);
	for (int i = m; i <= n; i++) {
		if (is_prime(i) == 1) {
			only_prime[prime_count] = i;
			prime_count++;
		}
	}

	int sum = only_prime[0];
	int min = only_prime[0];
	for (int i = 1; i < prime_count; i++) {
		sum += only_prime[i];
		if (min > only_prime[i]) {
			min = only_prime[i];
		}
	}

	if (only_prime[0] == 0) { //소수가 없으면
		printf("-1\n");
	}
	else {
		printf("%d\n%d\n", sum, min);
	}
	


	return 0;
}