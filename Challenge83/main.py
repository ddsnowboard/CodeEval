from sys import argv
import re
with open(argv[1], 'r') as f:
	not_letters = re.compile(r"[^a-z]")
	for l in f:
		current_line = not_letters.sub("",l.lower()).strip("\n")
		print(current_line)
	input()