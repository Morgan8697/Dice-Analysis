
import pygsheets as gsheets
import TakingOnlyThrees as tot
import TakingThreesAndOnes  as tto
import TakingOnesLast2 as toL2
import TakingOnesLast3 as toL3
import TakingOnesLast2Two as toL2t
import TakingOnesLast3Two as toL3t
import pandas as pd

SHEET_KEY = "1WxBKRVHFIMwIrBtrSB7CIoJDFIBBr3Ai7p3wGD22B6s"
MAX_ITERATIONS = 500000
ITERATIONS_FOR_SHEETS = 8000
UPDATE_SHEETS = False
client = gsheets.authorize(service_account_file='dicesdataanalysis-c336492d5528.json')
sheet = client.open_by_key(SHEET_KEY)
overviewInfoList = [] 
print('Simulation started...')
wSheetOverview = sheet[0]
#Taking Only Threes
print("1/6...")
if UPDATE_SHEETS:  
    wSheetThree = sheet[1]
    resultsThree = tot.sim(ITERATIONS_FOR_SHEETS)
    wSheetThree.set_dataframe(resultsThree, 'B1')
else:
    resultsThree = tot.sim(MAX_ITERATIONS)
    resultsThreeMean = resultsThree["Sum"].mean()
    firstDiceMean =     resultsThree["Dice #1"].mean()
    secondDiceMean =    resultsThree["Dice #2"].mean()
    thirdDiceMean =     resultsThree["Dice #3"].mean()
    fourthDiceMean =    resultsThree["Dice #4"].mean()
    fifthDiceMean =     resultsThree["Dice #5"].mean()
    highestValue =      resultsThree["Sum"].max()
    std =               resultsThree["Sum"].std()
    subset_df = resultsThree[resultsThree["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = resultsThree[resultsThree["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Mean": resultsThreeMean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns} 
    overviewInfoList.append(info)
#Taking Threes and Ones
print("2/6...")
if UPDATE_SHEETS:  
    wSheetThreeOne = sheet[2]
    resultsThreeOne = tto.sim(ITERATIONS_FOR_SHEETS)
    wSheetThreeOne.set_dataframe(resultsThreeOne,'B1')
else:
    resultsThreeOne = tto.sim(MAX_ITERATIONS)
    resultsThreeOneMean = resultsThreeOne["Sum"].mean()
    firstDiceMean =     resultsThreeOne["Dice #1"].mean()
    secondDiceMean =    resultsThreeOne["Dice #2"].mean()
    thirdDiceMean =     resultsThreeOne["Dice #3"].mean()
    fourthDiceMean =    resultsThreeOne["Dice #4"].mean()
    fifthDiceMean =     resultsThreeOne["Dice #5"].mean()
    highestValue =      resultsThreeOne["Sum"].max()
    std =               resultsThreeOne["Sum"].std()
    subset_df = resultsThree[resultsThreeOne["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = resultsThree[resultsThreeOne["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Mean": resultsThreeOneMean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns}
    overviewInfoList.append(info)
#Taking Ones for Last 2 Dices
print("3/6...")
if UPDATE_SHEETS:
    wSheetOneLast2 = sheet[3]  
    resultsOneLast2 = toL2.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast2.set_dataframe(resultsOneLast2,'B1')
else:
    resultsOneLast2 = toL2.sim(MAX_ITERATIONS)
    resultsOneLast2Mean = resultsOneLast2["Sum"].mean()
    firstDiceMean =     resultsOneLast2["Dice #1"].mean()
    secondDiceMean =    resultsOneLast2["Dice #2"].mean()
    thirdDiceMean =     resultsOneLast2["Dice #3"].mean()
    fourthDiceMean =    resultsOneLast2["Dice #4"].mean()
    fifthDiceMean =     resultsOneLast2["Dice #5"].mean()
    highestValue =      resultsOneLast2["Sum"].max()
    std =               resultsOneLast2["Sum"].std()
    subset_df = resultsOneLast2[resultsOneLast2["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = resultsOneLast2[resultsOneLast2["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Mean": resultsOneLast2Mean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns}
    overviewInfoList.append(info)
#Taking Ones for Last 3 Dices
print("4/6...")
if UPDATE_SHEETS:  
    wSheetOneLast3 = sheet[4]
    resultsOneLast3 = toL3.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast3.set_dataframe(resultsOneLast3,'B1')
else:
    resultsOneLast3 = toL3.sim(MAX_ITERATIONS)
    resultsOneLast3Mean = resultsOneLast3["Sum"].mean()
    firstDiceMean =     resultsOneLast3["Dice #1"].mean()
    secondDiceMean =    resultsOneLast3["Dice #2"].mean()
    thirdDiceMean =     resultsOneLast3["Dice #3"].mean()
    fourthDiceMean =    resultsOneLast3["Dice #4"].mean()
    fifthDiceMean =     resultsOneLast3["Dice #5"].mean()
    highestValue =      resultsOneLast3["Sum"].max()
    std =               resultsOneLast3["Sum"].std()
    subset_df = resultsOneLast3[resultsOneLast3["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = resultsOneLast3[resultsOneLast3["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Mean": resultsOneLast3Mean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns}
    overviewInfoList.append(info)
#Taking Ones for Last 2 Dices + Twos for last dice
print("5/6...")
if UPDATE_SHEETS:  
    wSheetOneLast2Two = sheet[5]
    resultsOneLast2Two = toL2t.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast2Two.set_dataframe(resultsOneLast2Two,'B1')
else:
    resultsOneLast2Two = toL2t.sim(MAX_ITERATIONS)
    resultsOneLast2TwoMean = resultsOneLast2Two["Sum"].mean()
    firstDiceMean =     resultsOneLast2Two["Dice #1"].mean()
    secondDiceMean =    resultsOneLast2Two["Dice #2"].mean()
    thirdDiceMean =     resultsOneLast2Two["Dice #3"].mean()
    fourthDiceMean =    resultsOneLast2Two["Dice #4"].mean()
    fifthDiceMean =     resultsOneLast2Two["Dice #5"].mean()
    highestValue =      resultsOneLast2Two["Sum"].max()
    std =               resultsOneLast2Two["Sum"].std()
    subset_df = resultsOneLast2Two[resultsOneLast2Two["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = resultsOneLast2Two[resultsOneLast2Two["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Mean": resultsOneLast2TwoMean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns}
    overviewInfoList.append(info)
#Taking Ones for Last 3 Dices + Twos for last dice
print("6/6...")
if UPDATE_SHEETS:  
    wSheetOneLast3Two = sheet[6]
    resultsOneLast3Two = toL3t.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast3Two.set_dataframe(resultsOneLast3Two,'B1')
else:
    resultsOneLast3Two = toL3t.sim(MAX_ITERATIONS)
    resultsOneLast3TwoMean = resultsOneLast3Two["Sum"].mean()
    firstDiceMean =     resultsOneLast3Two["Dice #1"].mean()
    secondDiceMean =    resultsOneLast3Two["Dice #2"].mean()
    thirdDiceMean =     resultsOneLast3Two["Dice #3"].mean()
    fourthDiceMean =    resultsOneLast3Two["Dice #4"].mean()
    fifthDiceMean =     resultsOneLast3Two["Dice #5"].mean()
    highestValue =      resultsOneLast3Two["Sum"].max()
    std =               resultsOneLast3Two["Sum"].std()
    subset_df = resultsOneLast3Two[resultsOneLast3Two["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = resultsOneLast3Two[resultsOneLast3Two["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Mean": resultsOneLast3TwoMean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns}
    overviewInfoList.append(info)
overviewDF = pd.DataFrame(overviewInfoList, columns=["Mean", "Dice #1 Average","Dice #2 Average","Dice #3 Average","Dice #4 Average","Dice #5 Average", "Highest Value", "Standard Deviation", "Percentage of good runs (<= 5)", "Percentage of bad runs (>= 10)"])
wSheetOverview.set_dataframe(overviewDF, 'B2')
print("Simulation over.")




