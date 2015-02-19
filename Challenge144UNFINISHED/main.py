# It works, but it's really slow for big n values. 
from sys import argv
from collections import defaultdict
def powers(a, n):
	x = 1
	current_output = a
	while x <= n:
		yield current_output
		current_output *= a
		x += 1
totals = defaultdict(int)
# import cProfile as pro
# pr = pro.Profile()
with open(argv[1], 'r') as f:
	for l in f:
		if l[0] == '#':
			continue
		# pr.enable()
		a, n = (int(p) for p in l.split(" "))
		# counter = 0
		for i in powers(a, n):
			totals[i%10]+=1
			# counter += 1
			# if counter == 1000:
				# print("{}\n\n".format(i))
				# counter = 0
		# pr.disable()
		# pr.print_stats()
		print(', '.join(['{}:{}'.format(i,totals[i]) for i in range(10)]))
input()