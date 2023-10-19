from Strategy import Strategy

STRATEGY_THRESHOLD = 3

class TakingOnlyThrees(Strategy):
    def __init__(self):
        super().__init__()

    def apply_strategy(self, current_dices):
        self.took_a_dice = False
        while 0 in current_dices:
            self.take_dice(0, current_dices)
        if not self.took_a_dice:
            self.take_dice(min(current_dices), current_dices)