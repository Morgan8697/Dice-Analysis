from Strategy import Strategy

STRATEGY_THRESHOLD = 3

class TakingOnesLast2(Strategy):
    def __init__(self):
        self.name = "Taking Ones for Last 2 dices"
        super().__init__()

    def apply_strategy(self, current_dices):
        self.took_a_dice = False
        while 0 in current_dices:
            self.take_dice(0, current_dices)
        while len(current_dices) < STRATEGY_THRESHOLD and 1 in current_dices:
            self.take_dice(1, current_dices)
        if not self.took_a_dice:
            self.take_dice(min(current_dices), current_dices)
