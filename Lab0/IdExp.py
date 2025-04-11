from Exp import Exp

class IdExp(Exp):
    def __init__(self, i):
        self.id = i

    def __repr__(self):
        return f'{self.id}'
