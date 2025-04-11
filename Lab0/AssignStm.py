from Stm import Stm

class AssignStm(Stm):
    def __init__(self, i, e):
        self.id = i
        self.exp = e

    def __repr__(self):
        return f'{self.id} := {self.exp}'

