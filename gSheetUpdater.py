from TakingOnlyThrees import MAX_ITERATIONS
import pygsheets as gsheets
import TakingOnlyThrees as tot
import TakingThreesAndOnes  as tto
import TakingOnesLast2 as toL2
import TakingOnesLast3 as toL3

SHEET_KEY = "1WxBKRVHFIMwIrBtrSB7CIoJDFIBBr3Ai7p3wGD22B6s"
MAX_ITERATIONS = 5000
client = gsheets.authorize(service_account_file='dicesdataanalysis-c336492d5528.json')
sheet = client.open_by_key(SHEET_KEY)

#Taking Only Threes
wSheetThree = sheet[0]
resultsThree = tot.sim(MAX_ITERATIONS)
wSheetThree.set_dataframe(resultsThree, 'B1')
#Taking Threes and Ones
wSheetThreeOne = sheet[1]
resultsThreeOne = tto.sim(MAX_ITERATIONS)
wSheetThreeOne.set_dataframe(resultsThreeOne,'B1')
#Taking Ones for Last 2 Dices
wSheetOneLast2 = sheet[2]
resultsOneLast2 = toL2.sim(MAX_ITERATIONS)
wSheetOneLast2.set_dataframe(resultsOneLast2,'B1')
#Taking Ones for Last 3 Dices
wSheetOneLast3 = sheet[3]
resultsOneLast3 = toL3.sim(MAX_ITERATIONS)
wSheetOneLast3.set_dataframe(resultsOneLast3,'B1')



