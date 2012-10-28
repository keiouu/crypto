#ifndef LANG_H
#define LANG_H 1

#include "common.h"

const float letter_distributions[] = {
	7.74582009897,
	1.48132394483,
	2.33371707206,
	4.57835744415,
	12.9484850026,
	2.19378343266,
	2.06170950208,
	6.99359973123,
	6.59198402167,
	0.101251543046,
	0.7827345314,
	4.07795598255,
	2.41524228708,
	6.81328876416,
	7.46826449924,
	1.51630735468,
	0.0972446326665,
	5.93161436878,
	6.45251271809,
	9.02371628609,
	2.78911784786,
	0.933456006436,
	2.45084214468,
	0.140858311026,
	1.98727343619,
	0.0895390357833
};

inline float* get_distributions(const char *str) {
	// Init
	float *dists = new float[26];
	for (int i = 0; i < 26; i++)
		dists[i] = 0;

	// Count
	for (int i = 0; i < strlen(str); i++)
		dists[(str[i] - 'A')]++;

	return dists;
}

#endif