#import library for operating system-agnostic file paths
import os

#import library for csv imports
import csv

#declare variables
total_votes = 0
candidates = []
vote_list = []
candidate_list = []
winner_list = []
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

# Open write file and start writing results
output_path = os.path.join("analysis", "results.txt")

with open(output_path, 'w', newline="") as output:

    output.write("Election Results")
    output.write('\n')
    output.write("-------------------------")
    output.write('\n')
    output.write(f"Total Votes: {total_votes}")
    output.write('\n')
    output.write("-------------------------")
    output.write('\n')


    # Iterate through unsorted list and print out the winners in order
    for vote in vote_list:
        top_vote = max(vote_list)
        winner_index = vote_list.index(top_vote)
        winner_list.append(candidate_list[winner_index])
        output.write(f"{candidate_list[winner_index]}: {percentage[winner_index]:3f}% ({top_vote})")
        output.write('\n')
        vote_list[winner_index] = 0
    
    output.write("-------------------------")
    output.write('\n')
    output.write(f"Winner: {winner_list[0]}")
    output.write('\n')
    output.write("-------------------------")
    output.write('\n')

# Print data on the terminal    
file = open(output_path, 'r')
print_output = file.read()   
print(print_output)
    


