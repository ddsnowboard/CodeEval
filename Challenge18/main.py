from sys import argv
with open(argv[1], 'r') as f:
	for i in f:
		x,orign = (int(p) for p in i.split(","))
		n = orign
		while n < x:
			n += orign
		print(n)