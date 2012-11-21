import ex3

ciphertext = "ZGHSTNXCAXAEYBQABTEMBNRKLLGWLKULEJRONQUIJMSDPUIIDWZFLIGKCHQNWHKLBHSIZLLMGHPRUFSWOIMHHMLZRZKTFKAXKLDRDPHIELQHPXUNRGWASHXLKRDSTXQNUHWKMZEEYMRETZQAWRBVDWOEZHFFKAMZLLHGAIYLJDVZEOWSDKLWAZRDVAIJMZGHYLUPENWBGQBYSKLYVIPQHKKKHQGHYFUWTBHZSGLENPHOKBEQRBKNEJZSWVUQTLDAIZHEGHJYZYZQHCITBYFZLEXTYCZOITLSDKHHJHYDWOMYTYCWOIVXYCDUXZHEGHUIIDWZFLLAGRHVVPGMPCDTMJMSDZOMZXYDVZSLAPQWOVUTEZVPXCTDCHZMMGPCWVHUAPRWLTVXOADJOZHDTUCIEAPQPFLKTGDQZWGBOBOHVKAZVELEAMTEXSCUNLQHHWKOPQBISJRVMRDWLBYDILEZAPQVTEQXQHQLFOKORDWIGLLMWNMXEMTWCIXRXNGLVGMPKBWVKIZRVLWYBYFWVXNXNZVBERHMRHYZKKTMKLVYBXOOLGUGOHWPSTTYCDAXOKPVLSPHEZNPHWGGLLDGMTZMDDBXEBQBOVXNXOZVHAUFLMRMJGLSHRUAOMSSKLEOWDSKHXGKEBDUVKGODUDLOEPSKLFKTFSBVJZAPLLKROZSSFYYYAHNXSHUYEDQJYZUFSDZSXKJELNYXXTESSEIXOHQZMJXEGHMMKEOVRTETLHQDWTKKFORUESHYNWVRUNDZFYIGZPNIAYXGTOVVRGWFKOKEEAPGDKRKOPQWPPRGZVHZXOFLSHKXNXLQWPWZBNDAJIREPMFLSLM"


def rotate(n):
	cutting_point = len(ciphertext) - (n % len(ciphertext))
	return ciphertext[cutting_point:] + ciphertext[:cutting_point]

def get_keylen():
	length = 4 # Min=4, Max=8
	kappas = []
	# We do kappa magic!
	for i in range(4, 9):
		tmp = rotate(i)
		coincidences = len([x for x in range(len(tmp)) if tmp[x] == ciphertext[x]]) # Coincidence? I think not!
		kappas.append(float(coincidences) / float(len(ciphertext)))

	best = -1
	for i in range(5):
		curr = (ex3.letterdists['kappa'] - kappas[i]) ** 2 # Squared
		if best == -1:
			best = curr
		if curr < best:
			length = 4 + i
			best = curr
	
	return length

if __name__ == "__main__":
	# Work out the key
	klen = get_keylen()
	code = ""
	for i in range(klen):
		# For every character in the key, work out what fits best with the
		# range of characters that key hashes
		letters = "".join([ciphertext[j] for j in range(i, len(ciphertext), klen)])
		shift = ex3.find_shift(letters)
		if shift == 0:
			code = "%sA" % code
		else:
			code = "%s%s" % (code, chr(ord('A') + (26 - shift)))
	print code
