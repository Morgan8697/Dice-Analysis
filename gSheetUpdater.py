
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

def produceDictStats(results):
    resultsMean = results["Sum"].mean()
    firstDiceMean =     results["Dice #1"].mean()
    secondDiceMean =    results["Dice #2"].mean()
    thirdDiceMean =     results["Dice #3"].mean()
    fourthDiceMean =    results["Dice #4"].mean()
    fifthDiceMean =     results["Dice #5"].mean()
    highestValue =      results["Sum"].max()
    std =               results["Sum"].std()
    subset_df = results[results["Sum"] <= 5]
    goodRuns =          subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    subset_df = results[results["Sum"] >= 10]
    badRuns =           subset_df.count()["Dice #1"]/MAX_ITERATIONS*100
    info = {"Average": resultsMean, "Dice #1 Average": firstDiceMean, "Dice #2 Average":secondDiceMean,"Dice #3 Average":thirdDiceMean,"Dice #4 Average":fourthDiceMean,"Dice #5 Average":fifthDiceMean,"Highest Value":highestValue,"Standard Deviation":std,"Percentage of good runs (<= 5)": goodRuns, "Percentage of bad runs (>= 10)": badRuns} 
    return info
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
    info = produceDictStats(resultsThree)
    overviewInfoList.append(info)
#Taking Threes and Ones
print("2/6...")
if UPDATE_SHEETS:  
    wSheetThreeOne = sheet[2]
    resultsThreeOne = tto.sim(ITERATIONS_FOR_SHEETS)
    wSheetThreeOne.set_dataframe(resultsThreeOne,'B1')
else:
    resultsThreeOne = tto.sim(MAX_ITERATIONS)
    info = produceDictStats(resultsThreeOne)
    overviewInfoList.append(info)
#Taking Ones for Last 2 Dices
print("3/6...")
if UPDATE_SHEETS:
    wSheetOneLast2 = sheet[3]  
    resultsOneLast2 = toL2.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast2.set_dataframe(resultsOneLast2,'B1')
else:
    resultsOneLast2 = toL2.sim(MAX_ITERATIONS)
    info = produceDictStats(resultsOneLast2)
    overviewInfoList.append(info)
#Taking Ones for Last 3 Dices
print("4/6...")
if UPDATE_SHEETS:  
    wSheetOneLast3 = sheet[4]
    resultsOneLast3 = toL3.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast3.set_dataframe(resultsOneLast3,'B1')
else:
    resultsOneLast3 = toL3.sim(MAX_ITERATIONS)
    info = produceDictStats(resultsOneLast3)
    overviewInfoList.append(info)
print("5/6...")
if UPDATE_SHEETS:  
    wSheetOneLast2Two = sheet[5]
    resultsOneLast2Two = toL2t.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast2Two.set_dataframe(resultsOneLast2Two,'B1')
else:
    resultsOneLast2Two = toL2t.sim(MAX_ITERATIONS)
    info = produceDictStats(resultsOneLast2Two)
    overviewInfoList.append(info)
#Taking Ones for Last 3 Dices + Twos for last dice
print("6/6...")
if UPDATE_SHEETS:  
    wSheetOneLast3Two = sheet[6]
    resultsOneLast3Two = toL3t.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast3Two.set_dataframe(resultsOneLast3Two,'B1')
else:
    resultsOneLast3Two = toL3t.sim(MAX_ITERATIONS)
    info = produceDictStats(resultsOneLast3Two)
    overviewInfoList.append(info)
overviewDF = pd.DataFrame(overviewInfoList, columns=["Average", "Dice #1 Average","Dice #2 Average","Dice #3 Average","Dice #4 Average","Dice #5 Average", "Highest Value", "Standard Deviation", "Percentage of good runs (<= 5)", "Percentage of bad runs (>= 10)"])
wSheetOverview.set_dataframe(overviewDF, 'B2')
print("Simulation over.")




