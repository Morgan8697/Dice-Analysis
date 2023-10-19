import random
import pandas as pd

def sim(iterations):
    iteration = 0
    dice_number = 5
    results_list = []
    while iteration < iterations:
        dices_taken = []
        while len(dices_taken) < dice_number:
            obtained_dices = []
            remaining_dices = dice_number - len(dices_taken)
            while len(obtained_dices) != remaining_dices:
                dice_value = random.randint(1,6)
                obtained_dices.append(dice_value)
            smallest_dice_value = 6
            dices_taken_last_number = len(dices_taken)
            for dice in obtained_dices:
                if dice < smallest_dice_value:
                    smallest_dice_value = dice
                if dice == 3:
                    dices_taken.append(dice)
                    remaining_dices -= 1
                if remaining_dices <= 2 and dice == 1:
                    dices_taken.append(dice)
                    remaining_dices -= 1
                if remaining_dices == 1 and dice == 2:
                    dices_taken.append(dice)
                    remaining_dices -= 1
            if dices_taken_last_number == len(dices_taken):
                dices_taken.append(smallest_dice_value)
        #transforming threes into 0
        dices_taken = [x if x != 3 else 0 for x in dices_taken]
        final_sum = sum(dices_taken)
        result = {"Dice #1" : dices_taken[0],"Dice #2" : dices_taken[1],"Dice #3" : dices_taken[2],"Dice #4" : dices_taken[3],"Dice #5" : dices_taken[4], "Sum": final_sum}
        results_list.append(result)
        iteration += 1
    one_and_three_results = pd.DataFrame(results_list, columns=["Dice #1","Dice #2","Dice #3","Dice #4","Dice #5", "Sum"])
    return one_and_three_results