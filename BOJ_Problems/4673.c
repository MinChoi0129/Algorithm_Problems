#include <stdio.h>

int d_num[10001] = { 0 };

void self_num() {
		
	int cal = 0;
	for (int i = 1; i <= 10000; i++) {
		if (i < 10) {
			cal = i + i;
			d_num[cal] = 1;
		}
		else if (i < 100) {
			cal = i + i / 10 + i % 10;
			d_num[cal] = 1;
		}
		else if (i < 1000) {
			cal = i + i / 100 + i % 100 / 10 + i % 100 % 10;
			d_num[cal] = 1;
		}
		else if (i < 10000) {
			cal = i + i / 1000 + i % 1000 / 100 + i % 1000 % 100 / 10 + i % 1000 % 100 % 10;
			if (cal <= 10000) {
				d_num[cal] = 1;
			}
		}
	}

	for (int i = 1; i <= 10000; i++) {
		if (d_num[i] == 0) {
			printf("%d\n", i);
		}
	}

}

int main() {
	
	self_num();

	return 0;
}