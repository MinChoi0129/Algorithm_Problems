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



int main() {

	int m, n;
	scanf("%d %d", &m, &n);
	for (int i = m; i <= n; i++) {
		if (is_prime(i)) {
			printf("%d\n", i);
		}
	}

	return 0;
}