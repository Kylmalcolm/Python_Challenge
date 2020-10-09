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

    profits = []
    for row in csvreader:
        profit = int(row[1])
        profits.append(profit)
        print(sum(profits))
        print(len(profits))



#months = sum(1 for row in csvreader)
#print(months)



        #in a loop, create a varaible outside of loop, set to zero,
        # and add 1 every time I'm in the loop
