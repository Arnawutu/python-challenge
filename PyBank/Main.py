# Import necessary modules
import os
import csv

# Create lists to store data
total_months = []
total_amount = []
average_change = []

# Set the path to the CSV file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
print(csvpath)

# Open the CSV file and specify encoding
with open(csvpath, encoding="utf-8") as csvfile:
    # Create a CSV reader
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    # Skip the header row
    csv_header = next(csvreader)
    # Populate the lists with data
    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))
    # Calculate the monthly profit/loss changes
    for i in range(len(total_amount) - 1):
        average_change.append(total_amount[i + 1] - total_amount[i])

# Calculate the greatest increase and decrease in profits
greatest_increase = max(average_change)
greatest_decrease = min(average_change)

# Find the months corresponding to the greatest increase and decrease
greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

# Print the financial analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: ${round(sum(average_change) / len(average_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${greatest_decrease})")

# Export the results to a text file
analysis = os.path.join("Financial_Analysis.txt")
with open(analysis, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_amount)}\n")
    file.write(f"Average Change: ${round(sum(average_change) / len(average_change), 2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${greatest_decrease})\n")