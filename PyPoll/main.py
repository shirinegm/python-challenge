#import library for operating system-agnostic file paths
import os

#import library for csv imports
import csv

#declare variables
total_votes = 0
candidates = []
vote_list = []
candidate_list = []
votes = []
percentage = []


#store the file using the file location
file_path = os.path.join("Resources", "election_data.csv")
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)

    # Iterate through the file to create candidates list
    for row in csv_reader:
        candidates.append(row[2])
    
    # Calculate total votes
    total_votes = len(candidates)

    # Get unique list of candidates
    candidate_list = set(candidates)

    # Count number of votes for each candidate
    for candidate in candidate_list:
        votes = candidates.count(candidate)
        vote_list.append(votes)
        percentage.append((votes/total_votes)*100)

candidate_list = list(candidate_list)

for vote in vote_list:
    top_vote = max(vote_list)
    winner_index = vote_list.index(top_vote)
    print(f"{candidate_list[winner_index]}: {percentage[winner_index]:3f}% ({top_vote})")
    vote_list[winner_index] = 0
    #del candidate_list[winner_index]
    #del percentage[winner_index]
    #print(candidate_list)
    # print(percentage)

    


