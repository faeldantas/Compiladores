from ExpList import ExpList

class PairExpList(ExpList):
	def __init__(self, h, t):
		self.head = h
		self.tail = t
	
	def __repr__(self):
		return f'{self.head}, {self.tail}'

