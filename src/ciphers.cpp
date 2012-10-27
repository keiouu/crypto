
#include "common.h"
#include "ciphers.h"
#include "../etc/tess26.h"

const char alpha[] = { "ABCDEFGHIJKLMNOPQRSTUVWXYZ" };

void rotate(int count, char *str) {
	int len = strlen(str);
 
	for (int i = 0; i < len; i++) {
		if (!isalpha(str[i]) || (str[i] == ' '))
			continue;
 
 		char lower = tolower(str[i]) - 'a';
		str[i] = alpha[((int)(lower) + count) % 26];
	}
}

void solve_caesar(const char *in) {
	char str[840];
	strcpy(str, in);

	printf("Decrypting %s\n", str);

	for (int i = 0; i < 26; i++) {

		rotate(1, str);
		if (strstr(tess26, str) != NULL) {
			printf("Solved by shifting %d places. \n", i + 1);
			printf("%s\n", str);
			break;
		}
	}
}

void solve_vigenere_with_key(const char *key, const char *in) {
	printf("Decrypting %s with key: %s\n", in, key);

	int len = strlen(in), k_len = strlen(key);
	char str[len];
	strcpy(str, in);

	for (int i = 0; i < len; i++) {
 		char lower = tolower(str[i]) - 'a';
 		char lkey = tolower(key[i % k_len]) - 'a';
 		int r = (int)(lower) - (int)lkey;
 		if (r < 0)
 			r = 26 + r;

		str[i] = alpha[r % 26];
	}

	printf("%s\n", str);
}