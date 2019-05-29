#import csv file and The total number of months included in the dataset
import csv 
input_File ="C:\\Users\\Karla Salome\\Desktop\\COLNYC201904DATA3\\homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv"
totalMonths = 0
totalRev = 0
pastRev = 0
highestIncRev = 0
lowestDecRev = 0
#create lists to store revenue change. [] saves it as a list.
revChange=[]

with open(input_File, newline='') as csvfile:
    #read file
    #split the data on commas
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #skip header row one time
    next(budget_csvreader)
    for row in budget_csvreader:
        #count total months in csv file
        totalMonths = totalMonths + 1
        #count total revenue in csv file using float in case there are decimal points
        totalRev = totalRev + (float(row[1]))
        #create a variable that will count the revenue change also with float
        monthlyRevChange = float(row[1]) - pastRev
        pastRev = float(row[1])
        #calculate the average change in revenue
        avgRevChange = totalRev/totalMonths
        #find the greatest increase in revenue
        if monthlyRevChange > highestIncRev:
            highestIncMonth = row[0]
            highestIncRev = monthlyRevChange 
        #find the greatest decrease in revenue
        if monthlyRevChange < lowestDecRev:
            lowestDecMonth = row[0]
            lowestDecRev = monthlyRevChange

#print everything, add '$' to currency

print("Karla Salome Pratts -FINANCIAL ANALYSIS-")
print("_____________________________________")
print(f"Total Months: {totalMonths}")
print(f"Total Revenue: ${totalRev}")
print(f"Average Revenue Change: ${avgRevChange}")
print(f"Greatest Increase in Revenue: {highestIncMonth} ${highestIncRev}")
print(f"Greatest Decrease in Revenue: {lowestDecMonth} ${lowestDecRev}")


