#include <stdio.h>
#include <math.h>

int is_prime(int n) {
	if (n <= 1) {
		return 0;
	}
	else if (n % 2 == 0) {
		return n == 2 ? 1 : 0;
	}

	else {
		for (int i = 3; i <= sqrt(n); i += 2) {
			if (n % i == 0) {
				return 0;
			}
		}
		return 1;
	}
}

int prime_count_from_n_to_2n(int n) {
	int count = 0;
	for (int i = n+1; i < 2*n; i++) {
		if (is_prime(i)) {
			count++;
		}
	}
	return count;
}

int main() {

	while (1) {
		int n;
		scanf("%d", &n);
		if (n == 0) {
			break;
		}
		else if (n == 1) {
			printf("1\n");
		}
		else {
			printf("%d\n", prime_count_from_n_to_2n(n));
		}
	}	

	return 0;
}