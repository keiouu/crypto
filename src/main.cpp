
#include "common.h"
#include "ciphers.h"

// Bring in header files
#include "../in/ex1.h"
#include "../in/ex2.h"
#include "../in/ex3.h"


int main(int argc, char *argv[]) {
	//solve_caesar(ex1);
	//solve_vigenere_with_key("TESSOFTHEDURBERVILLES", ex2);
	solve_vigenere_with_key_length(6, ex3);
}