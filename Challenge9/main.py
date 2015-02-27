class Stack(list):
	def __init__(self, *list):
		list.__init__(self)
		for i in list:
			self.append(i)
	def push(self, i):
		self.append(i)
from sys import argv
with open(argv[1]) as f:
	s = Stack()
	for i in f:
		for p in i.split(' '):
			s.push(int(p))
		while len(s) > 0:
			print(s.pop(), end=" ")
			try:
				s.pop()
			except IndexError:
				break
		print("")