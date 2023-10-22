from Strategy import Strategy

STRATEGY_THRESHOLD_ONES = 4
STRATEGY_THRESHOLD_TWOS = 2

class TakingOnesLast3Two(Strategy):
    def __init__(self):
        self.name = "Taking ones for last 3 dices and two for last"
        super().__init__()

    def apply_strategy(self, current_dices):
        self.took_a_dice = False
        while 0 in current_dices:
            self.take_dice(0, current_dices)
        while len(current_dices) < STRATEGY_THRESHOLD_ONES and 1 in current_dices:
            self.take_dice(1, current_dices)
        while len(current_dices) < STRATEGY_THRESHOLD_TWOS and 2 in current_dices:
            self.take_dice(2, current_dices)
        if not self.took_a_dice:
            self.take_dice(min(current_dices), current_dices)