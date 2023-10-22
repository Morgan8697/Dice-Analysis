
import pygsheets as gsheets
from Simulator import simulate_multiples
import DataParser
from TakingOnlyThrees import TakingOnlyThrees
from TakingThreesAndOnes import TakingThreesAndOnes
from TakingOnesLast2 import TakingOnesLast2
from TakingOnesLast3 import TakingOnesLast3
from TakingOnesLast2Two import TakingOnesLast2Two
from TakingOnesLast3Two import TakingOnesLast3Two
import pandas as pd

from Constant import ITERATIONS

SHEET_KEY = "1WxBKRVHFIMwIrBtrSB7CIoJDFIBBr3Ai7p3wGD22B6s"
MAX_ITERATIONS = 500000
ITERATIONS_FOR_SHEETS = 8000
UPDATE_SHEETS = False

#def produce_dict_stats(results):
#    results_mean = results["Sum"].mean()
#    first_dice_mean = results["Dice #1"].mean()
#    second_dice_mean = results["Dice #2"].mean()
#    third_dice_mean = results["Dice #3"].mean()
#    fourth_dice_mean = results["Dice #4"].mean()
#    fifth_dice_mean = results["Dice #5"].mean()
#    highest_value = results["Sum"].max()
#    std = results["Sum"].std()
#    subset_df = results[results["Sum"] <= 5]
#    good_runs = subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
#    subset_df = results[results["Sum"] >= 10]
#    bad_runs = subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
#    info = {"Average": results_mean, "Dice #1 Average": first_dice_mean, "Dice #2 Average": second_dice_mean, "Dice #3 Average": third_dice_mean, "Dice #4 Average": fourth_dice_mean, "Dice #5 Average": fifth_dice_mean, "Highest Value": highest_value, "Standard Deviation": std, "Percentage of good runs (<= 5)": good_runs, "Percentage of bad runs (>= 10)": bad_runs} 
#    return info
#
#client = gsheets.authorize(service_account_file='dicesdataanalysis-c336492d5528.json')
#sheet = client.open_by_key(SHEET_KEY)
#overview_info_list = [] 
#print('Simulation started...')
#w_sheet_overview = sheet[0]
#
## Taking Only Threes
#print("1/6...")
#tot = TakingOnlyThrees()
#if UPDATE_SHEETS:  
#    w_sheet_three = sheet[1]
#    results_three = tot.sim(ITERATIONS_FOR_SHEETS)
#    w_sheet_three.set_dataframe(results_three, 'B1')
#else:
#    results_three = tot.sim(MAX_ITERATIONS)
#    info = produce_dict_stats(results_three)
#    overview_info_list.append(info)
#
## Taking Threes and Ones
#print("2/6...")
#tto = TakingThreesAndOnes()
#if UPDATE_SHEETS:  
#    w_sheet_three_one = sheet[2]
#    results_three_one = tto.sim(ITERATIONS_FOR_SHEETS)
#    w_sheet_three_one.set_dataframe(results_three_one, 'B1')
#else:
#    results_three_one = tto.sim(MAX_ITERATIONS)
#    info = produce_dict_stats(results_three_one)
#    overview_info_list.append(info)
#
## Taking Ones for Last 2 Dices
#print("3/6...")
#tol2 = TakingOnesLast2()
#if UPDATE_SHEETS:
#    w_sheet_one_last_2 = sheet[3]  
#    results_one_last_2 = tol2.sim(ITERATIONS_FOR_SHEETS)
#    w_sheet_one_last_2.set_dataframe(results_one_last_2, 'B1')
#else:
#    results_one_last_2 = tol2.sim(MAX_ITERATIONS)
#    info = produce_dict_stats(results_one_last_2)
#    overview_info_list.append(info)
#
## Taking Ones for Last 3 Dices
#print("4/6...")
#tol3 = TakingOnesLast3()
#if UPDATE_SHEETS:  
#    w_sheet_one_last_3 = sheet[4]
#    results_one_last_3 = tol3.sim(ITERATIONS_FOR_SHEETS)
#    w_sheet_one_last_3.set_dataframe(results_one_last_3, 'B1')
#else:
#    results_one_last_3 = tol3.sim(MAX_ITERATIONS)
#    info = produce_dict_stats(results_one_last_3)
#    overview_info_list.append(info)
#
#print("5/6...")
#tol2t = TakingOnesLast2Two()
#if UPDATE_SHEETS:  
#    w_sheet_one_last_2_two = sheet[5]
#    results_one_last_2_two = tol2t.sim(ITERATIONS_FOR_SHEETS)
#    w_sheet_one_last_2_two.set_dataframe(results_one_last_2_two, 'B1')
#else:
#    results_one_last_2_two = tol2t.sim(MAX_ITERATIONS)
#    info = produce_dict_stats(results_one_last_2_two)
#    overview_info_list.append(info)
#
## Taking Ones for Last 3 Dices + Twos for last dice
#print("6/6...")
#tol3t = TakingOnesLast3Two()
#if UPDATE_SHEETS:  
#    w_sheet_one_last_3_two = sheet[6]
#    results_one_last_3_two = tol3t.sim(ITERATIONS_FOR_SHEETS)

def main():
    tol2 = TakingOnesLast2()
    ttao = TakingThreesAndOnes()
    to3 = TakingOnlyThrees()
    tol2t = TakingOnesLast2Two()
    tol3t = TakingOnesLast3Two()
    tol3 = TakingOnesLast3()

    strategies = [tol2, ttao, to3, tol2t, tol3t, tol3]
    
    simulate_multiples(ITERATIONS, strategies)
    
    df = DataParser.compute_stats(strategies)
    
    print(df)

    client = gsheets.authorize(service_account_file='dicesdataanalysis-c336492d5528.json')
    sheet = client.open_by_key(SHEET_KEY)
    
    sheet = sheet[0]
    
    sheet.set_dataframe(df, start = 'A2')
    
if __name__ == "__main__":
    main()
    

    
    