from sys import argv
from collections import defaultdict
with open(argv[1], 'r') as f:
	for i in f:
		a, n = (int(p) for p in i.split(" "))
		totals = defaultdict(int)
		for i in [a**x for x in range(n+1)]:
			totals[str(i)[-1]]+=1
# Make it print all the numbers, even the ones that don't show up. 
# https://www.codeeval.com/open_challenges/144/
print(':'.join(['{}, {}'.format(i,j) for i, j in totals.items()]))