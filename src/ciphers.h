#ifndef CIPHERS_H
#define CIPHERS_H 1

void solve_caesar(const char *in);

void attempt_vigenere(const char *key, const char *in, char* out);
void solve_vigenere_with_key(const char *key, const char *in);
void solve_vigenere_with_key_length(int len, const char *in);

#endif