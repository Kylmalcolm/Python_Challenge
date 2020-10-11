import os
import csv

budget_csv = os.path.join("..", "Resources", "Test.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    candidate_list = []

    counter = 0

    counter0 = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0

    for row in csvreader:

        candidate = row[2]

        counter = counter + 1
        candidate_list.append(candidate)   

        candidate_list = list(dict.fromkeys(candidate_list))

        if candidate == candidate_list[0]:
            counter0 = counter0 + 1
        elif candidate == candidate_list[1]:
            counter1 = counter1 + 1
        elif candidate == candidate_list[2]:
            counter2 = counter2 + 1
        elif candidate == candidate_list[3]:
            counter3 = counter3 + 1

print(counter)
print(candidate_list)
print(counter0)
print(counter1)
print(counter2)
print(counter3)