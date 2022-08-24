#include <stdio.h>
#include <string.h>

int main() {

	char word[100];
	scanf("%s", word);
	int len = strlen(word);
	
	int count = 0;
	for (int i = 0; i < len; i++) {
		if (word[i] == 'c') {
			if (word[i + 1] == '=') {
				count++;
				i++;
			}
			else if (word[i + 1] == '-') {
				count++;
				i++;
			}
			else {
				count++;
			}
		}
		else if (word[i] == 'd') {
			if (word[i + 1] == '-') {
				count++;
				i++;
			}
			else if (word[i + 1] == 'z' && word[i + 2] == '=') {
				count++;
				i += 2;
			}
			else {
				count++;
			}
		}
		else if (word[i] == 'l') {
			if (word[i + 1] == 'j') {
				count++;
				i++;
			}
			else {
				count++;
			}
		}
		else if (word[i] == 'n') {
			if (word[i + 1] == 'j') {
				count++;
				i++;
			}
			else {
				count++;
			}
		}
		else if (word[i] == 's') {
			if (word[i + 1] == '=') {
				count++;
				i++;
			}
			else {
				count++;
			}
		}
		else if (word[i] == 'z') {
			if (word[i + 1] == '=') {
				count++;
				i++;
			}
			else {
				count++;
			}
		}
		else {
			count++;
		}
	}

	printf("%d\n", count);

	return 0;
}