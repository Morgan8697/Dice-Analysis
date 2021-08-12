import pandas as pd
import random
MAX_ITERATIONS = 1000
DICE_NUMBER = 5

#Taking ones and threes every turn

def sim(iterations):
    iteration = 0

    resultsList = []
    while iteration < iterations:
        dicesTaken = []
        while len(dicesTaken) < DICE_NUMBER:
            obtainedDices = []
            remainingDices = DICE_NUMBER - len(dicesTaken)
            while len(obtainedDices) != remainingDices:
                diceValue = random.randint(1,6)
                obtainedDices.append(diceValue)
            smallestDiceValue = 6
            dicesTakenLastNumber = len(dicesTaken)
            for dice in obtainedDices:
                if dice < smallestDiceValue:
                    smallestDiceValue = dice
                if dice == 3:
                    dicesTaken.append(dice)
            if dicesTakenLastNumber == len(dicesTaken):
                dicesTaken.append(smallestDiceValue)
        #transforming threes into 0
        dicesTaken = [x if x != 3 else 0 for x in dicesTaken]
        finalSum = sum(dicesTaken)
        result = {"De #1" : dicesTaken[0],"De #2" : dicesTaken[1],"De #3" : dicesTaken[2],"De #4" : dicesTaken[3],"De #5" : dicesTaken[4], "Somme": finalSum}
        resultsList.append(result)
        iteration += 1
    oneAndThreeResults = pd.DataFrame(resultsList, columns=["De #1","De #2","De #3","De #4","De #5", "Somme"])
    return oneAndThreeResults
