#include <stdio.h>

int main() {

	int case_num;
	scanf("%d", &case_num);
	for (int i = 0; i < case_num; i++) {
		char arr[20];
		for (int a = 0; a < 20; a++) {
			arr[a] = '\0';
		}
		int times;
		scanf("%d %s", &times, arr);
		for (int j = 0; j < 20; j++) {
			for (int k = 0; k < times; k++) {
				if (arr[j] != '\0') {
					printf("%c", arr[j]);
				}
			}
		}
		printf("\n");
	}


	return 0;
}