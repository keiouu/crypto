
#include "common.h"
#include "ciphers.h"

void rotate(int count, char *str) {
	int length = strlen(str);
	char alpha[2][27] = { "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
 
	for (int i = 0; i < length; i++) {
		if (!isalpha(str[i]) || (str[i] == ' '))
			continue;
 
 		int isUpper = isupper(str[i]);
 		if (isUpper > 1)
 			isUpper = 1;
 		char lower = tolower(str[i]) - 'a';
		str[i] = alpha[isUpper][((int)(lower) + count) % 26];
	}
}

void solve_caesar(const char *in) {
	char str[840];
	strcpy(str, in);

	printf("Decrypting %s\n", str);

	for (int i = 0; i < 26; i++) {
		rotate(1, str);
		printf("%s\n", str);
	}
}