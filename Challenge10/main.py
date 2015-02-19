from sys import argv
with open(argv[1],'r') as f:
	for i in f:
		try:
			l = list(i.replace("\n",'').split(' '))
			print(l[:-1][-1*int(l[-1])])
		except IndexError:
			pass