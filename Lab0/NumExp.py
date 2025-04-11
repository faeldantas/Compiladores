from Exp import Exp

class NumExp(Exp):
    def __init__(self, n):
        self.num = n
    def __repr__(self):
        return f'{self.num}'

