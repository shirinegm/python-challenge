#import library for operating system-agnostic file paths
import os

#import library for csv imports
import csv

#store the file using the file location
file_path = os.paht.join("..", "Resources", "election_data.csv")
with open(file_path) as csv_file:
    csv_reader = csv.reader(csf_file)
