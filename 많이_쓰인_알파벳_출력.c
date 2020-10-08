#include <stdio.h>
#include <string.h>

char word[1000000];
char largeword[1000000];

int main() {

	int aphb_count[26] = { 0 };
	gets(word);
	int len = strlen(word);
	for (int i = 0; i < len; i++) {
		if ('a' <= word[i] && word[i] <= 'z') {
			largeword[i] = word[i] - 32;
		}
		if ('A' <= word[i] && word[i] <= 'Z') {
			largeword[i] = word[i];
		}
	}



	for (int i = 0; i < len; i++) {
		for (char j = 'A'; j <= 'Z'; j++) {
			if (largeword[i] == j) {
				aphb_count[j - 'A']++;
				break;
			}
		}
	}

	int max = -1, remember = -1;
	for (int i = 0; i < 26; i++) {
		if (max < aphb_count[i]) {
			max = aphb_count[i];
			remember = i;
		}
	}

	int count = 0;
	for (int i = 0; i < 26; i++) {
		if (max == aphb_count[i]) {
			count++;
		}
	}	


	if (count > 1) {
		printf("?\n");
	}
	else {
		printf("%c\n", remember + 'A');
	}


	return 0;
}