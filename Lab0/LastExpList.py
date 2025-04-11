from ExpList import ExpList

class LastExpList(ExpList):
    def __init__(self, h):
        self.head = h
    def __repr__(self):
        return f'{self.head}'
