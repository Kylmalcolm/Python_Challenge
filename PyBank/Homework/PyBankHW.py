import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #dates = []
    #profits = []
    #changes = []
        #I eventually figured out how to use lists for this, but stuck with my original solution
        #and left them as comments because I need to sleep sometime tonight

    counter = 0
    total = 0
    increase = 0
    decrease = 0
    diff_profit = 0
    sum_changes = 0

    for row in csvreader:

        date = row[0]
        #dates.append(row[0])

        profit = row[1]
        #profits.append(int(row[1]))

        counter = counter + 1
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
        
        if diff_profit == 0:
            diff_profit = int(profit)
        else:
            diff_profit = int(profit) - int(diff_profit)
            #changes.append(int(diff_profit))
            sum_changes = int(sum_changes) + int(diff_profit)
            diff_profit = int(profit)
            
avg_changes = sum_changes / (int(counter) - 1)
avg_changes = round(avg_changes,2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(counter))
print("Total: $" + str(total))
print("Average Change: $" + str(avg_changes))
print("Greatest Increase in Profits: " + str(increase_date) + " $" + str(increase))
print("Greatest Decrease in Profits: " + str(decrease_date) + " $" + str(decrease))

filename = 'PyBank_Output.txt'

with open(filename, 'w') as file_object:
    file_object.write("Financial Analysis\n")
    file_object.write("----------------------------\n")
    file_object.write("Total Months: " + str(counter) +"\n")
    file_object.write("Total: $" + str(total) + "\n")
    file_object.write("Average Change: $" + str(avg_changes) + "\n")
    file_object.write("Greatest Increase in Profits: " + str(increase_date) + " $" + str(increase) + "\n")
    file_object.write("Greatest Decrease in Profits: " + str(decrease_date) + " $" + str(decrease) + "\n")

#sum_profits = sum(profits)
#print(sum_profits)