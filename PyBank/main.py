#import library for operating system-agnostic file paths
import os

#import library for csv imports
import csv

#define variables
total_months = 0
total_net = 0
profit_loss = 0
change = 0
change_list = [0]
avg_chage = 0
greatest_increase = 0
greatest_decrease = 0

#store the file using the file location
file_path = os.path.join("Resources", "budget_data.csv")
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)

    # Iterate through rows to collect data
    for row in csv_reader:
        total_months = total_months + 1
        change = profit_loss
        profit_loss = int(row[1])
        total_net = total_net + profit_loss
        change_list.append(profit_loss - change)

    
    
def average(list):
    return sum(list) / len(list)
del change_list[0]
del change_list[0]
average_change = average(change_list)


print("Financial Analysis")
print("------------------------------------")
print(f"Total Months {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change}")
# print(change_list)

