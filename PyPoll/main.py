#import library for operating system-agnostic file paths
import os

#import library for csv imports
import csv

#declare variables
total_votes = 0
candidates_list = []
index = 0

#store the file using the file location
file_path = os.path.join("Resources", "election_data.csv")
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)

    for row in csv_reader:
        index = index + 1
        total_votes = total_votes + 1
        current_candidate = row[2]
        if current_candidate not in candidates_list:
            candidates_list.append(current_candidate)


print(total_votes)
print(candidates_list)