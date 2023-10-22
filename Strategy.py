from Constant import DICE_NUMBER, POSSIBLE_DICES
from random import *

class Strategy:
    def __init__(self):
        self.score = 0
        self.total_score = 0
        self.taken_dices = []
        self.took_a_dice = False

    def apply_strategy(self):
        pass

    def take_dice(self, dice, current_dices):
        self.taken_dices.append(dice)
        current_dices.remove(dice)
        self.score += dice
        self.took_a_dice = True

    def play(self, dices):
        self.score = 0
        self.taken_dices = []
        while len(self.taken_dices) < DICE_NUMBER:
            self.apply_strategy(dices)
            dices = [choice(POSSIBLE_DICES) for d in range(DICE_NUMBER - len(self.taken_dices))]
        self.total_score += self.score