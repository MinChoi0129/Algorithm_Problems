#include <stdio.h>
#include <math.h>

int primes[1229];

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

void show_GCD(int a, int b) { // 최대공약수
	int result = 1;
	for (int i = 0; i < 1229; i++) {
		while (a % primes[i] == 0 && b % primes[i] == 0) {
			result *= primes[i];
			a /= primes[i];
			b /= primes[i];
		}
	}
	printf("%d\n", result);
}

void show_LCM(int a, int b) { // 최소공배수
	int result = 1;
	for (int i = 0; i < 1229; i++) {
		while (a % primes[i] == 0 && b % primes[i] == 0) {
			result *= primes[i];

			a /= primes[i];
			b /= primes[i];

		}
	}

	result = result * a * b;
	printf("%d\n", result);
}

int main() {

	set_prime(primes);
	int a, b;
	scanf("%d %d", &a, &b);
	show_GCD(a, b);
	show_LCM(a, b);


	return 0;
}