import math
def primes():
	yield 2
	prime = True
	out = 3
	while True:
		prime = True
		for i in range(2, int(math.sqrt(out))+1):
			if out%i==0:
				prime = False
		if prime:
			yield out
		out+=2
end = 0
p = primes()
for i in range(1000):
	end+=next(p)
print(end)