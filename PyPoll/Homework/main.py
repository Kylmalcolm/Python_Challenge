import os
import csv

budget_csv = os.path.join("..", "Resources", "election_data.csv")

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

    percentage0 = counter0 / counter
    percentage0 = "{0:.3%}".format(percentage0)
    percentage1 = counter1 / counter
    percentage1 = "{0:.3%}".format(percentage1)
    percentage2 = counter2 / counter
    percentage2 = "{0:.3%}".format(percentage2)
    percentage3 = counter3 / counter
    percentage3 = "{0:.3%}".format(percentage3)

winner_tally = {candidate_list[0] : counter0, candidate_list[1] : counter1, 
candidate_list[2] : counter2, candidate_list[3] : counter3}

winner = max(winner_tally, key=winner_tally.get)

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(counter))
print("----------------------------")
print(str(candidate_list[0]) + ": " + str(percentage0) + " (" + str(counter0) + ")")
print(str(candidate_list[1]) + ": " + str(percentage1) + " (" + str(counter1) + ")")
print(str(candidate_list[2]) + ": " + str(percentage2) + " (" + str(counter2) + ")")
print(str(candidate_list[3]) + ": " + str(percentage3) + " (" + str(counter3) + ")")
print("----------------------------")
print("Winner: " + str(winner))
print("----------------------------")

filename = 'PyPoll_Output.txt'

with open(filename, 'w') as file_object:

     file_object.write("Election Results\n")
     file_object.write("----------------------------\n")
     file_object.write("Total Votes: " + str(counter) +"\n")
     file_object.write("----------------------------\n")
     file_object.write(str(candidate_list[0]) + ": " + str(percentage0) + " (" + str(counter0) + ")\n")
     file_object.write(str(candidate_list[1]) + ": " + str(percentage1) + " (" + str(counter1) + ")\n")
     file_object.write(str(candidate_list[2]) + ": " + str(percentage2) + " (" + str(counter2) + ")\n")
     file_object.write(str(candidate_list[3]) + ": " + str(percentage3) + " (" + str(counter3) + ")\n")
     file_object.write("----------------------------\n")
     file_object.write("Winner: " + str(winner) + "\n")
     file_object.write("----------------------------\n")