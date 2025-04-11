from Exp import Exp

class CompoundStm(Exp):
    def __init__(self, s1, s2):
        self.stm1 = s1
        self.stm2 = s2

    def __repr__(self):
        return f'{self.stm1}; {self.stm2}'

