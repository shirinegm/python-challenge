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
date_list = []
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
        date_list.append(row[0])
        


# Define funtion to calculate the average    
def average(list):
    return sum(list) / len(list)


# Clean up the first two rows from the list
del change_list[0]
del change_list[0]
del date_list[0]
del date_list[0]

# Call average function
average_change = average(change_list)

# Find where the greatest increase is
index_increase = change_list.index(max(change_list))

# Find where the greatest decrease is
index_decrease = change_list.index(min(change_list))

# print out
# print("Financial Analysis")
# print("------------------------------------")
# print(f"Total Months {total_months}")
# print(f"Total: ${total_net}")
# print(f"Average Change: ${average_change:.2f}")
# print(f"Greatest Increase in Profits: {date_list[index_increase]} $({change_list[index_increase]})")
# print(f"Greatest Decrease in Profits: {date_list[index_decrease]} $({change_list[index_decrease]})")
# print(change_list)

# write output to file
output_path = os.path.join("analysis", "results.txt")

with open(output_path, 'w', newline='') as output:
    output.write("Financial Analysis")
    output.write('\n')
    output.write("------------------------------------")
    output.write('\n')
    output.write(f"Total Months {total_months}")
    output.write('\n')
    output.write(f"Total: ${total_net}")
    output.write('\n')
    output.write(f"Average Change: ${average_change:.2f}")
    output.write('\n')
    output.write(f"Greatest Increase in Profits: {date_list[index_increase]} $({change_list[index_increase]})")
    output.write('\n')
    output.write(f"Greatest Decrease in Profits: {date_list[index_decrease]} $({change_list[index_decrease]})")

file = open(output_path, 'r')
print_output = file.read()   
print(print_output)