from sys import argv
with open(argv[1]) as f:
	for i in f:
		print(sum([int(p) for p in i.strip("\n")]))