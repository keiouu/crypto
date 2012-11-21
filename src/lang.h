#ifndef LANG_H
#define LANG_H 1

#include "common.h"

const float letter_distributions[] = {
	7.74582009897,		// A
	1.48132394483,		// B
	2.33371707206,		// C
	4.57835744415,		// D
	12.9484850026,		// E
	2.19378343266,		// F
	2.06170950208,		// G
	6.99359973123,		// H
	6.59198402167,		// I
	0.101251543046,		// J
	0.7827345314,		// K
	4.07795598255,		// L
	2.41524228708,		// M
	6.81328876416,		// N
	7.46826449924,		// O
	1.51630735468,		// P
	0.0972446326665,	// Q
	5.93161436878,		// R
	6.45251271809,		// S
	9.02371628609,		// T
	2.78911784786,		// U
	0.933456006436,		// V
	2.45084214468,		// W
	0.140858311026,		// X
	1.98727343619,		// Y
	0.0895390357833		// Z
};

inline float* get_distributions(const char *str) {
	float t = (float)strlen(str);

	// Init
	float *dists = new float[26];
	for (int i = 0; i < 26; i++)
		dists[i] = 0.0f;

	// Count
	for (int i = 0; i < strlen(str); i++)
		if (str[i] != 0)
			dists[(str[i] - 'A')]++;

	// Distribute
	for (int i = 0; i < 26; i++)
		dists[i] = (dists[i] / t) * 100;

	return dists;
}

/**
 * Returns the index of the letter most likely to be e
 */
inline int get_e(float *dists) {
	int ptr = 0;
	float max = 0.0f;

	for (int i = 0; i < 26; i++) {
		if (dists[i] > max) {
			ptr = i;
			max = dists[i];
		}
	}

	return ptr;
}

#endif