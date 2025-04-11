from Exp import Exp

class OpExp(Exp):
	def __init__(self, _left, _oper, _right):
		self.left = _left
		self.oper = _oper
		self.right = _right
	def __repr__(self):
	    return f'{self.left}{self.oper}{self.right}'
