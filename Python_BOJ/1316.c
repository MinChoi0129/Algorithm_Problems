#include <stdio.h>
#include <string.h>

int main() {

	int n;
	scanf("%d", &n); // 케이스 개수
	int counting = 0; // 조건에 맞는 케이스 개수 카운팅
	for (int i = 0; i < n; i++) { // n개의 케이스 반복
		char word[100]; // 단어 입력받기
		char alphabet_lock[26] = { 0 };
		scanf("%s", word);
		int len = strlen(word);
		for (int i = 0; i < len; i++) {
			for (char j = 'a'; j <= 'z'; j++) {
				if (word[i] == j) {
					if (word[i] != word[i + 1]) {
						alphabet_lock[j - 'a']++;
					}
				}
			}
		}
		int max = 0;
		for (int i = 0; i < 26; i++) {
			if (alphabet_lock[i] > max) {
				max = alphabet_lock[i];
			}
		}
		if (max == 1) {
			counting++;
		}
	}

	printf("%d\n", counting);
	
	return 0;
}