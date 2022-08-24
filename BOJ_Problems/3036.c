#include <stdio.h>
#include <math.h>

int primes[1229];

int show_GCD(int a, int b) { // 최대공약수
	int result = 1;
	for (int i = 0; i < 1229; i++) {
		while (a % primes[i] == 0 && b % primes[i] == 0) {
			result *= primes[i];
			a /= primes[i];
			b /= primes[i];
		}
	}
	return result;
}

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

void set_prime(int arr[]) {
	int count = 0;
	for (int i = 2; i <= 10000; i++) {
		if (is_prime(i)) {
			arr[count] = i;
			count++;
		}
	}
}

int main() {
	
	set_prime(primes);

	int n;
	scanf("%d", &n);
	int* wheel_r = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &wheel_r[i]);
	}

	for (int i = 1; i < n; i++) {
		int gcd = show_GCD(wheel_r[0], wheel_r[i]);

		printf("%d/%d\n", wheel_r[0] / gcd, wheel_r[i] / gcd);
	}

	return 0;
}