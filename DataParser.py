from Constant import DICE_NUMBER
import pandas as pd
import numpy as np

def compute_stats(strategies):
    df = pd.DataFrame()
    for strategy in strategies:
        means = compute_dices_means(strategy)
        good_runs = sum(score <= 5 for score in strategy.all_scores) / len(strategy.all_scores) * 100
        bad_runs = sum(score >= 10 for score in strategy.all_scores) / len(strategy.all_scores) * 100
        stats = {
            "Strategy": strategy.name,
            "Average": strategy.mean, 
            "Dice #1 Average": means["Dice #1"], 
            "Dice #2 Average": means["Dice #2"], 
            "Dice #3 Average": means["Dice #3"], 
            "Dice #4 Average": means["Dice #4"], 
            "Dice #5 Average": means["Dice #5"], 
            "Highest Value": max(strategy.all_scores), 
            "Standard Deviation": np.std(strategy.all_scores), 
            "Percentage of good runs (<= 5)": good_runs, 
            "Percentage of bad runs (>= 10)": bad_runs}
        df = pd.concat([df, pd.DataFrame(stats, index=[0])])
    return df
    
def compute_dices_means(strategy):
    first_dice_total = 0
    second_dice_total = 0
    third_dice_total = 0
    fourth_dice_total = 0
    fifth_dice_total = 0
    for i in range(len(strategy.total_taken_dices)):
        if i % DICE_NUMBER == 0:
            first_dice_total += strategy.total_taken_dices[i]
        elif i % DICE_NUMBER == 1:
            second_dice_total += strategy.total_taken_dices[i]
        elif i % DICE_NUMBER == 2:
            third_dice_total += strategy.total_taken_dices[i]
        elif i % DICE_NUMBER == 3:
            fourth_dice_total += strategy.total_taken_dices[i]
        elif i % DICE_NUMBER == 4:
            fifth_dice_total += strategy.total_taken_dices[i]
    first_mean = first_dice_total/len(strategy.all_scores)
    second_mean = second_dice_total/len(strategy.all_scores)
    third_mean = third_dice_total/len(strategy.all_scores)
    fourth_mean = fourth_dice_total/len(strategy.all_scores)
    fifth_mean = fifth_dice_total/len(strategy.all_scores)
    
    return {"Dice #1": first_mean, "Dice #2": second_mean, "Dice #3": third_mean, "Dice #4": fourth_mean, "Dice #5": fifth_mean}