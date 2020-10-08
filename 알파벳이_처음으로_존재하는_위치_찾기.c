#include <stdio.h>

int main() {

	char word[100] = { 0 };
	int exist[26] = { 0 };
	for (int i = 0; i < 26; i++) {
		exist[i] = -1;
	}
	scanf("%s", word);
	for (int i = 0; i < 100; i++) {
		for (char j = 'a'; j <= 'z'; j++) {
			if (exist[j - 97] == -1) {
				if (word[i] == j) {
					exist[j - 97] = i;
					continue;
				}
			}
		}
	}

	for (int i = 0; i < 26; i++) {
		printf("%d ", exist[i]);
	}


	return 0;
}