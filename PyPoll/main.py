import os
import csv
from collections import Counter

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv') 

#create lists, variables
votes = []
candidate = []
w = 0

#opening csv file
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
#voting count, unique candidate list and votes 
    for row in csv.reader(csvfile):
        votes.append(row[0])
        candidate.append(row[2])
    vote_count = len(votes)
    counter = Counter(candidate)
    candidate_name = list(counter.keys())
    individual_votes = list(counter.values())

    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {(vote_count)}")
    print(f"----------------------------")

#looping for percentage calculation
    for i in range (len(candidate_name)):
        per = (individual_votes[i]/vote_count)*100   
        print(f"{candidate_name[i]}: {format(per,'.3f')}% ({individual_votes[i]})")

#looping for higher value
    for i in range(1, len(individual_votes)):
        if individual_votes[i] > individual_votes[w]:
            w = i
        winner = candidate_name[w]
    print(f"----------------------------")
    print(f"Winner: {winner}")
    print(f"----------------------------")

output_path = os.path.join("..", "PyPoll", "results.txt")

with open(output_path, 'w', newline='') as datafile:

    csvwriter = csv.writer(datafile, delimiter=',')
    csvwriter.writerow([(f"Election Results")])
    csvwriter.writerow([(f"----------------------------")])
    csvwriter.writerow([(f"Total Votes: {(vote_count)}")])
    csvwriter.writerow([(f"----------------------------")])
    for i in range (len(candidate_name)):
        per = (individual_votes[i]/vote_count)*100  
        csvwriter.writerow([(f"{candidate_name[i]}: {format(per,'.3f')}% ({individual_votes[i]})")])
    csvwriter.writerow([(f"----------------------------")])
    csvwriter.writerow([(f"Winner: {winner}")])
    csvwriter.writerow([(f"----------------------------")])
