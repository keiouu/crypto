
#include "common.h"
#include "ciphers.h"
#include "lang.h"
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

void attempt_vigenere(const char *key, const char *in, char* out) {
	int len = strlen(in), k_len = strlen(key);
	strcpy(out, in);

	for (int i = 0; i < len; i++) {
 		char lower = tolower(out[i]) - 'a';
 		char lkey = tolower(key[i % k_len]) - 'a';
 		int r = (int)(lower) - (int)lkey;
 		if (r < 0)
 			r = 26 + r;

		out[i] = alpha[r % 26];
	}
}

void solve_vigenere_with_key(const char *key, const char *in) {
	printf("Decrypting %s with key: %s\n", in, key);
	int len = strlen(in);
	char out[len];
	attempt_vigenere(key, in, out);
	printf("%s\n", out);
}

void solve_vigenere_with_key_length(int klen, const char *in) {
	int in_len = strlen(in);

	// We know the key length, lets do some frequency analysis to find the key
	char *proposed_key = new char[klen];

	for (int i = 0; i < klen; i++) {
		// Build a char of all the letters this part of the key has hashed
		char *keystr = new char[in_len / klen];
		int ptr = 0;
		for (int j = i; j < in_len; j+=klen)
			keystr[ptr++] = in[j];

		// Get the distributions for this key
		float *dists = get_distributions(keystr);


		// Try to find 'E'
		int lk = get_e(dists);

		// E is supposed to be 4, what letter must be added to this to make lk?
		if (lk - 4 >= 0) 
			proposed_key[i] = 'A' + (lk - 4);
		else
			proposed_key[i] = 'Z' + (lk - 4);

		delete keystr;
		delete dists;
	}


	solve_vigenere_with_key(proposed_key, in);
	delete proposed_key;
}