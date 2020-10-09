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
    changes = []

    counter = 0
    total = 0
    increase = 0
    decrease = 0

    for row in csvreader:
        date = row[0]
        dates.append(date)

        profit = row[1]
        profits.append(int(profit))

        counter = counter +1
        total = total + int(profit)

        if int(increase) > int(profit):
            increase = increase
        else:
            increase = int(profit)
            increase_date = date

        if int(decrease) < int(profit):
            decrease = decrease
        else:
            decrease = int(profit)
            decrease_date = date
        
    #for profit in profits_list:
        #change = 

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(counter))
print("Total: $" + str(total))
print("Average Change: $")
print("Greatest Increase in Profits: " + str(increase_date) + " $" + str(increase))
print("Greatest Decrease in Profits: " + str(decrease_date) + " $" + str(decrease))

print(changes)

#DON'T FORGET THE EXPORT STEP!!!!!

        #in a loop, create a varaible outside of loop, set to zero,
        # and add 1 every time I'm in the loop