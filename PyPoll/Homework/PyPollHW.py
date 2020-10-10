import os
import csv

budget_csv = os.path.join("..", "Resources", "election_data.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    counter = 0

    for row in csvreader:

        voter = row[0]
        county = row[1]
        candidate = row[2]

        counter = counter + 1

        

print(counter)


        