from sys import argv
import re
from collections import Counter
from functools import reduce
not_letters = re.compile(r"[^a-z]")
with open(argv[1], 'r') as f:
	for l in f:
		current_line = not_letters.sub("",l.lower())
		c = Counter(current_line)
		scores = {}
		next_score = 26
		for i in [j[0] for j in c.most_common()]:
			scores[i] = next_score
			next_score -= 1
		print(reduce(lambda x, y: x + scores[y], current_line, 0))