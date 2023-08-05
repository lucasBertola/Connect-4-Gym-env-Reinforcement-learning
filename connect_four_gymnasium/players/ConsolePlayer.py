from .Player import Player

class ConsolePlayer(Player):

    def __init__(self, _=""):
        pass
    
    def play(self, _):
        move = -1
        while move < 1 or move > 7:
            try:
                move = int(input("Enter a move between 1 and 7: "))
                if move < 1 or move > 7:
                    print("The move must be between 1 and 7.")
            except ValueError:
                print("Please enter an integer.")
        return move -1

    def getName(self):
        return "ConsolePlayer"

    def isDeterministic(self):
        return False
    
    def getElo(self):
        return None