from random import choice
from Constant import DICE_NUMBER, POSSIBLE_DICES

def sim(iterations, strategy):
    for i in range(iterations):
        starting_dices = [choice(POSSIBLE_DICES) for d in range(DICE_NUMBER)]
        strategy.play(starting_dices)
    strategy.mean = strategy.total_score / iterations
    strategy.iterations = iterations

def simulate_multiples(iterations, strategies):
    print("Simulation started...")
    for strategy in strategies:
        print("Simulating " + strategy.name + "...")
        sim(iterations, strategy)