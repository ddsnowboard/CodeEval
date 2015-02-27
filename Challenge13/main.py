from sys import argv
with open(argv[1]) as f:
	for i in f:
		line, letters = i.split(", ")
		for l in letters:
			line = line.replace(l, '')
		print(line)