
import pygsheets as gsheets
import TakingOnlyThrees as tot
import TakingThreesAndOnes  as tto
import TakingOnesLast2 as toL2
import TakingOnesLast3 as toL3
import TakingOnesLast2Two as toL2t
import TakingOnesLast3Two as toL3t

SHEET_KEY = "1WxBKRVHFIMwIrBtrSB7CIoJDFIBBr3Ai7p3wGD22B6s"
MAX_ITERATIONS = 500000
ITERATIONS_FOR_SHEETS = 8000
UPDATE_SHEETS = False
client = gsheets.authorize(service_account_file='dicesdataanalysis-c336492d5528.json')
sheet = client.open_by_key(SHEET_KEY)
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
    gsheets.Cell("J3",val=resultsThreeMean, worksheet=wSheetOverview).set_value(resultsThreeMean) 
#Taking Threes and Ones
print("2/6...")
if UPDATE_SHEETS:  
    wSheetThreeOne = sheet[2]
    resultsThreeOne = tto.sim(ITERATIONS_FOR_SHEETS)
    wSheetThreeOne.set_dataframe(resultsThreeOne,'B1')
else:
    resultsThreeOne = tto.sim(MAX_ITERATIONS)
    resultsThreeOneMean = resultsThreeOne["Sum"].mean()
    gsheets.Cell("J4",val=resultsThreeOneMean, worksheet=wSheetOverview).set_value(resultsThreeOneMean) 
#Taking Ones for Last 2 Dices
print("3/6...")
if UPDATE_SHEETS:
    wSheetOneLast2 = sheet[3]  
    resultsOneLast2 = toL2.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast2.set_dataframe(resultsOneLast2,'B1')
else:
    resultsOneLast2 = toL2.sim(MAX_ITERATIONS)
    resultsOneLast2Mean = resultsOneLast2["Sum"].mean()
    gsheets.Cell("J5",val=resultsOneLast2Mean, worksheet=wSheetOverview).set_value(resultsOneLast2Mean) 
#Taking Ones for Last 3 Dices
print("4/6...")
if UPDATE_SHEETS:  
    wSheetOneLast3 = sheet[4]
    resultsOneLast3 = toL3.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast3.set_dataframe(resultsOneLast3,'B1')
else:
    resultsOneLast3 = toL3.sim(MAX_ITERATIONS)
    resultsOneLast3Mean = resultsOneLast3["Sum"].mean() 
    gsheets.Cell("J6",val=resultsOneLast3Mean, worksheet=wSheetOverview).set_value(resultsOneLast3Mean)
#Taking Ones for Last 2 Dices + Twos for last dice
print("5/6...")
if UPDATE_SHEETS:  
    wSheetOneLast2Two = sheet[5]
    resultsOneLast2Two = toL2t.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast2Two.set_dataframe(resultsOneLast2Two,'B1')
else:
    resultsOneLast2Two = toL2t.sim(MAX_ITERATIONS)
    resultsOneLast2TwoMean = resultsOneLast2Two["Sum"].mean()
    gsheets.Cell("J7",val=resultsOneLast2TwoMean, worksheet=wSheetOverview).set_value(resultsOneLast2TwoMean) 
#Taking Ones for Last 3 Dices + Twos for last dice
print("6/6...")
if UPDATE_SHEETS:  
    wSheetOneLast3Two = sheet[6]
    resultsOneLast3Two = toL3t.sim(ITERATIONS_FOR_SHEETS)
    wSheetOneLast3Two.set_dataframe(resultsOneLast3Two,'B1')
else:
    resultsOneLast3Two = toL3t.sim(MAX_ITERATIONS)
    resultsOneLast3TwoMean = resultsOneLast3Two["Sum"].mean()
    gsheets.Cell("J8",val=resultsOneLast3TwoMean, worksheet=wSheetOverview).set_value(resultsOneLast3TwoMean)
print("Simulation over.")



