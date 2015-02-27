from sys import argv
from collections import defaultdict
with open(argv[1]) as f:
	for i in f:
		# print(i)
		dict = {}
		for n in i.split(','):
			dict[n.replace('\n', '')] = True
		print(",".join(sorted([i for i,j in dict.items() if j], key = lambda x: int(x))))