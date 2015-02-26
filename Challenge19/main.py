from sys import argv
with open(argv[1], 'r') as f:
	for i in f:
		num, p1, p2 = (int(p) for p in i.split(","))
		if (num & 2**(p1-1) == 0) == (num & 2**(p2-1) == 0):
			print('true')
		else:
			print('false')