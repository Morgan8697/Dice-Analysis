from Strategy import Strategy

STRATEGY_THRESHOLD = 3

class TakingThreesAndOnes(Strategy):
    def __init__(self):
        self.name = "Taking Threes and Ones"
        super().__init__()

    def apply_strategy(self, current_dices):
        self.took_a_dice = False
        taken_dices_one_turn = []
        for dice in current_dices:
            if dice == 0 or dice == 1:
                taken_dices_one_turn.append(dice)
        for dice in taken_dices_one_turn:
            self.take_dice(dice, current_dices)
        if not self.took_a_dice:
            self.take_dice(min(current_dices), current_dices)