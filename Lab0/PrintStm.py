from Stm import Stm

class PrintStm(Stm):
	def __init__(self, e):
		self.exps = e
		
	def __repr__(self):
		return f'print({self.exps})'
	