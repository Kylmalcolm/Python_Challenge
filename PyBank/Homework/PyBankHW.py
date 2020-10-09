import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#def budget_info(budget_data):

   #date = str(budget_data[0])
   #profit = int(budget_data[1])

   #return


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    dates = []
    profits = []
    counter = 0
    total = 0
    for row in csvreader:
        date = row[0]
        dates.append(date)
        profit = row[1]
        profits.append(int(profit))
        counter = counter +1
        total = total + int(profit)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(counter))
print("Total: $" + str(total))
print("Average Change: $")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

        #in a loop, create a varaible outside of loop, set to zero,
        # and add 1 every time I'm in the loop