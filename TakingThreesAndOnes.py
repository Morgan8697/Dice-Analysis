from Strategy import Strategy

STRATEGY_THRESHOLD = 3

class TakingThreesAndOnes(Strategy):
    def __init__(self):
        super().__init__()

    def apply_strategy(self, current_dices):
        self.took_a_dice = False
        for dice in current_dices:
            if dice is 0:
                self.take_dice(0, current_dices)
            elif dice is 1:
                self.take_dice(1, current_dices)
        if not self.took_a_dice:
            self.take_dice(min(current_dices), current_dices)