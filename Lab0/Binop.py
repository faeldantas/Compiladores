from Exp import Exp

class Binop(Exp):
    plus = '+'
    minus = '-'
    times = '*'
    div ='/'
    def __init__(self, _value):
        self.VALUE = _value

    def __repr__(self):
        return f'{self.VALUE}'

