import pandas as pd
import random
DICE_NUMBER = 5

#Taking ones last 2 dices
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
                    remainingDices -= 1
                if remainingDices <= 2 and dice == 1:
                    dicesTaken.append(dice)
                    remainingDices -= 1
                if remainingDices == 1 and dice == 2:
                    dicesTaken.append(dice)
                    remainingDices -= 1
            if dicesTakenLastNumber == len(dicesTaken):
                dicesTaken.append(smallestDiceValue)
        #transforming threes into 0
        dicesTaken = [x if x != 3 else 0 for x in dicesTaken]
        finalSum = sum(dicesTaken)
        result = {"Dice #1" : dicesTaken[0],"Dice #2" : dicesTaken[1],"Dice #3" : dicesTaken[2],"Dice #4" : dicesTaken[3],"Dice #5" : dicesTaken[4], "Sum": finalSum}
        resultsList.append(result)
        iteration += 1
    oneAndThreeResults = pd.DataFrame(resultsList, columns=["Dice #1","Dice #2","Dice #3","Dice #4","Dice #5", "Sum"])
    return oneAndThreeResults
