
intxt = "JILCBGHINYWTXSNVQRSYAUVRELAFQUSXEHPWDIUYAVLHSUVSOXDYIBRYHUZVZPHIEGLRZFQBPWKZPWDECYLOYGAMBCCWDULGFGYYMRPHPIBVPMNLMWRREHPWDJWWMHHIJNGMPENMJSQSNYBVPMNNQAPMSUAWWPKPMFELALMMZYGHWKSIOUQRTEIUTZCMCBBBZAWMQTSSSYDSCXKZIZDMBSBVTWWMASCXEIVVTWHYOGDIAGMRESCCDSHEUUVRSIOOLRPRHSAOEHKQVHZWWPMVTQOYTTQVKGNOWPEHOWEAWMWBWCWMTWRLPUBHLGGINTLMJNVSDWNYAIWXEHOTCSINPSEIZCWIDHWSAXZYNHMMLRZNPSPBYCBSXIJNWTLVNCDOWLWMIBJPANBSCGKGMTZVIYTOEIHSPSLWGYLWCIYYQJPHPBMZLWPSWIDIJNWBMCPBMAPVAMBQSEJWMOYHWZBSCGKHAWOINUJZPHAFIMELNICUSFACVUTRHUVRZVEGQUSXDUDSNSIYACZRALQHHEOZZCXCKOZKTJAQMGFTLIASOMPQIGZRHSWBPSPBMFSEZLMQPRPFGQZQANPSJLWXVCEWAHBWESJNWVTQGHWKTRCBMKZYHXAHLVPZWFSSIYACDSKHPSSEONQZJSLYVSOXDYTSEXALXFZHQWMRLRZQIGXYYBLWDXQLJSOXKLMOOMJNMGDWDUVRHVENQBRXDYASYXEGMBEWARXFPWOYLWYLALTODXDOZFTIZMKFLAHNWVTQKQPMSERYGCFXNYIHPHIYACXSJMBFZYOFGOYKAFQRZRKNLSDINPMWEMDUDSELKOOVEMPUTZZZALKO"

letterdists = {
	"A": 7.74582009897,	
	"B": 1.48132394483,	
	"C": 2.33371707206,	
	"D": 4.57835744415,	
	"E": 12.9484850026,	
	"F": 2.19378343266,	
	"G": 2.06170950208,	
	"H": 6.99359973123,	
	"I": 6.59198402167,	
	"J": 0.101251543046,	
	"K": 0.7827345314,	
	"L": 4.07795598255,	
	"M": 2.41524228708,	
	"N": 6.81328876416,	
	"O": 7.46826449924,	
	"P": 1.51630735468,	
	"Q": 0.0972446326665,
	"R": 5.93161436878,	
	"S": 6.45251271809,	
	"T": 9.02371628609,	
	"U": 2.78911784786,	
	"V": 0.933456006436,	
	"W": 2.45084214468,	
	"X": 0.140858311026,	
	"Y": 1.98727343619,	
	"Z": 0.0895390357833,
	"max": 12.9484850026,
	"kappa":0.0666
}

# Shift all letters by key
def c_shift(txt, shift):
	out = ''
	for i in range(len(txt)):
		letter = txt[i]
		out = "%s%s" % (out, chr((ord(letter) - ord('A') + shift) % 26 + ord('A')))
	return out

# Create a letter distributions table
def count_freqs(txt):
	freqs = {}
	for l in txt:
		freqs[l] = freqs.get(l, 0) + 1
	return freqs

# Convert a letter dist table into percentables for comparison
def freq_pcnt(freqs):
	vals = freqs.values()
	vals.sort()
	max_val = vals[-1]
	for (k, v) in freqs.items():
		freqs[k] = v * (letterdists['max'] / max_val)
	return freqs

# Convert a letter dist dict into norm deviation dict
def norm_deviant(freqs):
	t = 0
	for (k, v) in freqs.items():
		t += (v - letterdists[k]) ** 2 # Squared
	return t

# Find the shift that brings us closer to the letterdists
def find_shift(txt):
	best = 0

	smallest = -1
	for shift in range(26):
		encoded = c_shift(txt, shift)
		freqs = count_freqs(encoded)
		freqs = freq_pcnt(freqs)
		deviation = norm_deviant(freqs)

		if smallest == -1:
			smallest = deviation

		if deviation < smallest:
			best = shift
			smallest = deviation

	return best

if __name__ == "__main__":
	# Work out the key
	klen = 6
	code = ""
	for i in range(klen):
		# For every character in the key, work out what fits best with the
		# range of characters that key hashes
		letters = "".join([intxt[j] for j in range(i, len(intxt), klen)])
		shift = find_shift(letters)
		if shift == 0:
			code = "%sA" % code
		else:
			code = "%s%s" % (code, chr(ord('A') + (26 - shift)))
	print code