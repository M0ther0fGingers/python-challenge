# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
profits = 0
change_pnl = 0
average_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
row_count = 0
net_change_list = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')
    
    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    row_count += 1
    profits += int(first_row[1])
    prev_val = int(first_row[1])
    
    # count all the rows to get the total months
    for row in reader:
        row_count += 1

    # Track the total and net change
        profits += int(row[1])
        net_change = int(row[1]) - prev_val
        net_change_list.append(net_change)
        prev_val = int(row[1])

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    avg_monthly_change = sum(net_change_list)/(len(net_change_list))     


# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {row_count}
Total: ${profits:,.2f} 
Average Change: ${avg_monthly_change:,.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})
"""


# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)