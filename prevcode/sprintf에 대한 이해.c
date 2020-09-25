#include <stdio.h>

int main() {

	int a, b, c, mul;
	int count[10] = { 0 };
	char tostring[10];
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	mul = a * b * c;
	sprintf(tostring, "%d", mul);
	for (int i = 0; i < 10; i++) {
		if (tostring[i] == '0') {
			count[0]++;
		}
		else if (tostring[i] == '1') {
			count[1]++;
		}
		else if (tostring[i] == '2') {
			count[2]++;
		}
		else if (tostring[i] == '3') {
			count[3]++;
		}
		else if (tostring[i] == '4') {
			count[4]++;
		}
		else if (tostring[i] == '5') {
			count[5]++;
		}
		else if (tostring[i] == '6') {
			count[6]++;
		}
		else if (tostring[i] == '7') {
			count[7]++;
		}
		else if (tostring[i] == '8') {
			count[8]++;
		}
		else if (tostring[i] == '9') {
			count[9]++;
		}
		else {
		}
	}
	for (int j = 0; j < 10; j++) {
		printf("%d\n", count[j]);
	}


	return 0;
}