import os
import csv

budget_csv = os.path.join("..", "Resources", "Test.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    candidate_list = []

    counter = 0

    for row in csvreader:
        voter = row[0]
        county = row[1]
        candidate = row[2]

        counter = counter + 1
        candidate_list.append(candidate)

individual_votes = 0        
candidate_dict = dict.fromkeys(candidate_list)

# for row in csvreader:
#     if candidate in candidate_dict:
#         candidate_dict[candidate] = individual_votes + 1

print(counter)
print(candidate_dict)

        