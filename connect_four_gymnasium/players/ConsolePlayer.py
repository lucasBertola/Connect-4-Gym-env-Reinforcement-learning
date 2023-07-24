from .Player import Player

class ConsolePlayer(Player):

    def __init__(self, _=""):
        pass
    
    def play(self, _):
        move = -1
        while move < 0 or move > 6:
            try:
                move = int(input("Enter a move between 0 and 6: "))
                if move < 0 or move > 6:
                    print("The move must be between 0 and 6.")
            except ValueError:
                print("Please enter an integer.")
        return move

    def getName(self):
        return "ConsolePlayer"

    def isDeterministic(self):
        return False
    
    def getElo(self):
        return None