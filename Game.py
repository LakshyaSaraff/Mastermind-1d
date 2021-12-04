import random as r
from Constants import Colors, guesses, code_length


class Game:
    def __init__(self, guess):
        self.code = []  
        self.guess = guess
    def createCode(self):
        for i in range(code_length):
            self.code.append(r.choice(Colors.keys()))

    def Update(self):
        pass
    def checkCode(self):
        if self.code == self.guess:
            return True
        return False
    def Pegs(self):
        pass