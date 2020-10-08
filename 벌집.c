#include <stdio.h>

int room_count(int n) {

	int i=1;
	n--;
	while (n > 0) {
		n -= 6 * i;
		i++;
	}

	return i;
}

int main() {

	int n;
	scanf("%d", &n);
	printf("%d\n", room_count(n));

	return 0;
}