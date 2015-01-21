# Make a sieve, and then go through it and find all the palindromes, and then print the highest out out.
def sieve(n):
	l = (n+1) * [True]
	for i, j in enumerate(l):
		if i == 0:
			l[i] = False
			continue
		elif i == 1:
			l[i] = None
			continue
		if j:
			p = 2
			while i*p <= n:
				l[i*p] = False
				p += 1
	return l
print(max([i[0] for i in enumerate(sieve(1000)) if (str(i[0]) == str(i[0])[::-1]) and (i[1])]))