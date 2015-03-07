from sys import argv
with open(argv[1]) as f:
	for i in f:
		print(str(bin(int(i)))[2:].count('1'))