import math

ciphertext = "IATHBOEAOIALTOTAEEIHGTOHOKHPDFBCAMIUYRMTEFVNADNHOHNEDTEKEGLDDWESERAWENOEPBTRHYVSCEBTLASRDOIEEAIIASGBEOAYPENTALEREMCINARLOSMNAIODWNAOTESTCERLEUFMICHLTUTRIELDIHEOSPUAOOCGTINLYAVIOTTHTICEOSIAERFWOTPIAOEDNDETKVUTHNDROTEWFSFLNIHUIISSDEGEHOTIEEGHOESATGAOAOCOEGRWSANIDPAONLHIAATHNOROSASEDSPAOVEHEALHEIYREYYWNARKNRPAIURDTPOSGHSORIRPOTATELOAAGUFTAOOSNHATAANWEBTTIGRWDETARGIAIDELMWPPMTUREUPALHDELWIEEICENFSMNAEYENOENLOSBOESHIEBIEGCEUTAOOEBLTKAGTDSSHSEDEWUNUREEDSTKRHPXTTURNWAHHDESTENTEAUSTMHIEFTAISIDOTECSERENIAOAFOEVBKSETSEEDENRTYEERSSTEUBVNSLNINTWBMNZBTCHSMFHWTIHRNDHTEYHDHUOONBSYUFCNEFDAREOOOSEORSDDENRLEMDASELCTSBDTSORLAAALMAUNATILYENWBLIGOLNRTRISETHSTYAEUSTRTCTPEORIOOEOLPIEHTEIENEEDTAHNTHCCNOEIETSHHTTDGTHEDKUYMASDRWUUUAEONFFHMFBSATLVMRLESIOCASEHIEDODIILAAIEYLEAAFIIHDATREIHAOENTSUFCUOFRPESTIWNARNNNAAFNOUAHETNSATRTXLEELSFUIUEYPRBRHITORINOOSTIO"

#abcdefghijklmno

#a b c d e
#f g h i j
#k l m n o

#afkbglchmdinejo
#afk bgl chm din ejo



def try_column(column):
	# Split into blocks
	blk_len = len(ciphertext) / column
	blks = [ciphertext[i:i+blk_len] for i in range(0, len(ciphertext), blk_len)]

	# Print out
	ostr = ""
	for i in range(0, blk_len):
		for blk in blks:
			ostr = ostr + blk[i]
	print ostr

try_column(4)
try_column(5)
try_column(6)
try_column(7)
try_column(8)
