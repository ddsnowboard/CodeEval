from sys import argv 
with open(argv[1], 'r') as f:
	num = int(f.readline())
	print("\n".join(sorted([i for i in f.readlines()], key=len, reverse=True)[:num]))