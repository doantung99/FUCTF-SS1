from Crypto.Util.number import *
import itertools
import string

with open("enc.txt", "r") as f:
    data = f.read().split(", ")
enc_lst = []
for i in range(len(data)):
    enc_lst.append(long(data[i]))

def s2n(s):
	return bytes_to_long(s)

def n2s(n):
    return long_to_bytes(n)


p1 = s2n("fuct")
characters = list(string.digits + string.uppercase + string.lowercase + "{._!?}")
for i, j in itertools.permutations(characters, 2):
	p2 = s2n("f{"+i+j)
	if(enc_lst[0] - p2) % p1 == 0:
		key = (enc_lst[0] - p2) / p1
		enc = [p1]
		for i in range(0,8):
			enc += [enc_lst[i] - enc[i]*key]
		for i in range(len(enc)):
			enc[i] = n2s(enc[i])
		print ''.join(enc)
