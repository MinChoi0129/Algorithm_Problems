#include <stdio.h>
#include <math.h>

int prime_num_arr[1229];
int possible[5000][2];
int gap[5000];
void print_goldbach_partition();
void alloc_prime_num();
int is_prime(int n);


int main() {

	alloc_prime_num();


	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		print_goldbach_partition();
	}

	return 0;
}

void print_goldbach_partition(void) {

	int even_num;
	int count = 0;

	for (int i = 0; i < 5000; i++) {
		gap[i] = -10000;
		for (int j = 0; j < 2; j++) {
			possible[i][j] = -1;
		}
	}
	scanf("%d", &even_num);
	for (int i = 0; i < 1229; i++) {
		for (int j = 0; j < 1229; j++) {
			if (even_num == prime_num_arr[i] + prime_num_arr[j]) {
				possible[count][0] = prime_num_arr[i];
				possible[count][1] = prime_num_arr[j];
				gap[count] = prime_num_arr[j] - prime_num_arr[i];
				count++;
				if (prime_num_arr[j] > prime_num_arr[j]) {
					break;
				}
			}
		}
	}

	int min = 9999;
	int remember = 0;
	for (int i = 0; i < count; i++) {
		if (gap[i] >= 0) {
			if (min > gap[i]) {
				min = gap[i];
				remember = i;
			}
		}
	}
	printf("%d %d\n", possible[remember][0], possible[remember][1]);


}
void alloc_prime_num(void) {
	int count = 0;
	for (int i = 2; i <= 10000; i++) {
		if (is_prime(i)) {
			prime_num_arr[count] = i;
			count++;
			if (count == 1229) {
				return;
			}
		}
	}
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