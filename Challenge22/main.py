from sys import argv
class Fibs:
	def __init__(self):
		self.fibs = [0, 1, 1]
	def get(self, num):
		try:
			return self.fibs[num]
		except IndexError:
			while len(self.fibs) <= num:
				self.fibs.append(sum(self.fibs[-2:]))
			return self.get(num)
with open(argv[1]) as f:
	fibs = Fibs()
	for i in f:
		print(fibs.get(int(i)))