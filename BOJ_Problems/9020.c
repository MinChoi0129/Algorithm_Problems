#include <stdio.h>
#include <math.h>

int is_prime(int n);


int main() {

	int n;
	scanf("%d", &n);

	while (n--) {
		int even;
		scanf("%d", &even);
		int cut1 = even / 2;
		int cut2 = even / 2;
		while (1) {
			if (is_prime(cut1) && is_prime(cut2)) {
				printf("%d %d\n", cut1, cut2);
				break;
			}
			else {
				cut1 -= 1;
				cut2 += 1;
			}
		}
	}
	
	return 0;
}


int is_prime(int n) {
	if (n <= 1) { // 1이하는 소수 아님
		return 0;
	}
	else if (n % 2 == 0) { // 2를 제외한 짝수는 소수가 아님
		return n == 2 ? 1 : 0;
	}

	else {
		for (int i = 3; i <= sqrt(n); i += 2) { // 1을 제외한 홀수만 남았기 때문에 이 남은 홀수들만 판별.
			if (n % i == 0) {
				return 0;
			}
		}
		return 1;
	}
}