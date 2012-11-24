ciphertext = "ZGHSTNXCAXAEYBQABTEMBNRKLLGWLKULEJRONQUIJMSDPUIIDWZFLIGKCHQNWHKLBHSIZLLMGHPRUFSWOIMHHMLZRZKTFKAXKLDRDPHIELQHPXUNRGWASHXLKRDSTXQNUHWKMZEEYMRETZQAWRBVDWOEZHFFKAMZLLHGAIYLJDVZEOWSDKLWAZRDVAIJMZGHYLUPENWBGQBYSKLYVIPQHKKKHQGHYFUWTBHZSGLENPHOKBEQRBKNEJZSWVUQTLDAIZHEGHJYZYZQHCITBYFZLEXTYCZOITLSDKHHJHYDWOMYTYCWOIVXYCDUXZHEGHUIIDWZFLLAGRHVVPGMPCDTMJMSDZOMZXYDVZSLAPQWOVUTEZVPXCTDCHZMMGPCWVHUAPRWLTVXOADJOZHDTUCIEAPQPFLKTGDQZWGBOBOHVKAZVELEAMTEXSCUNLQHHWKOPQBISJRVMRDWLBYDILEZAPQVTEQXQHQLFOKORDWIGLLMWNMXEMTWCIXRXNGLVGMPKBWVKIZRVLWYBYFWVXNXNZVBERHMRHYZKKTMKLVYBXOOLGUGOHWPSTTYCDAXOKPVLSPHEZNPHWGGLLDGMTZMDDBXEBQBOVXNXOZVHAUFLMRMJGLSHRUAOMSSKLEOWDSKHXGKEBDUVKGODUDLOEPSKLFKTFSBVJZAPLLKROZSSFYYYAHNXSHUYEDQJYZUFSDZSXKJELNYXXTESSEIXOHQZMJXEGHMMKEOVRTETLHQDWTKKFORUESHYNWVRUNDZFYIGZPNIAYXGTOVVRGWFKOKEEAPGDKRKOPQWPPRGZVHZXOFLSHKXNXLQWPWZBNDAJIREPMFLSLM"

#a b c
#d e f
#g h i

#adgcfibeh

#adg
#cfi
#beh

#abc
#def
#ghi

def try_column(column):
	# Split into columns
	columns = [[ciphertext[x] for x in range(i, len(ciphertext), column)] for i in range(0, column)]

	stro = ""
	# Print each character, alternating between columns
	for i in range(0, len(ciphertext) / column):
		alt = False
		for j in range(0, len(columns)):
			if alt:
				stro += columns[j][i]
			else:
				stro += columns[len(columns) - 1 - j][i]

			alt = not alt



	# Re-order columns
	o_columns = []
	for i in range(0, len(columns)):
		if i > (len(columns) - 1 - i):
			break

		if i == (len(columns) - 1 - i):
			o_columns.append(columns[i])
			break

		o_columns.append(columns[i])
		o_columns.append(columns[len(columns) - 1 - i])

	stro = ""
	for i in range(0, max(map(lambda a: len(a), o_columns))):
		stro = stro + ''.join([x[i] for x in o_columns])
	print stro

try_column(4)
try_column(5)
try_column(6)
try_column(7)
try_column(8)