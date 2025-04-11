from Exp import Exp

class EseqExp(Exp):
	def __init__(self, s, e):
		self.stm = s
		self.exp = e
		
	def __repr__(self):
	    return f'({self.stm}, {self.exp})'
