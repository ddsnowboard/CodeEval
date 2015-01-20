# Make a sieve, and then go through it and find all the palindromes, and then print the highest out out.
def sieve(n):
    l = (n+1) * [True]
    for i, j in enumerate(l):
        if j:
            p = 2
            while i*p <= n:
                print(p)
                l[j] = False
                p += 1
    return l
