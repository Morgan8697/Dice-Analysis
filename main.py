from random import *
from Constant import DICE_NUMBER, POSSIBLE_DICES, ITERATIONS
from TakingOnesLast2 import TakingOnesLast2
from TakingThreesAndOnes import TakingThreesAndOnes
from TakingOnlyThrees import TakingOnlyThrees
from TakingOnesLast2Two import TakingOnesLast2Two
from TakingOnesLast3Two import TakingOnesLast3Two
from TakingOnesLast3 import TakingOnesLast3


def sim(iterations, strategy):
    for i in range(iterations):
        starting_dices = [choice(POSSIBLE_DICES) for d in range(DICE_NUMBER)]
        strategy.play(starting_dices)

def main():
    tol2 = TakingOnesLast2()
    ttao = TakingThreesAndOnes()
    to3 = TakingOnlyThrees()
    tol2t = TakingOnesLast2Two()
    tol3t = TakingOnesLast3Two()
    tol3 = TakingOnesLast3()

    sim(ITERATIONS, tol2)
    sim(ITERATIONS, ttao)
    sim(ITERATIONS, to3)
    sim(ITERATIONS, tol2t)
    sim(ITERATIONS, tol3t)
    sim(ITERATIONS, tol3)

    print("Moyenne TakingOnesLast2 :", tol2.total_score/ITERATIONS)
    print("Moyenne TakingThreesAndOnes :", ttao.total_score/ITERATIONS)
    print("Moyenne TakingOnlyThrees :", to3.total_score/ITERATIONS)
    print("Moyenne TakingOnesLast2Two :", tol2t.total_score/ITERATIONS)
    print("Moyenne TakingOnesLast3Two :", tol3t.total_score/ITERATIONS)
    print("Moyenne TakingOnesLast3 :", tol3.total_score/ITERATIONS)

if __name__ == "__main__":
    main()