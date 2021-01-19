# Import OS module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(r'''C:\Users\bisma\python-challenge\PyBank\Resources\budget_data.csv''')

# Read using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget_data = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(budget_data)

    # Declare global variables 
    first_row = next(budget_data)
    start_rev = first_row[1]
    total = int(start_rev)
    num_rows = 1
    dates = [first_row[0]]
    prof_loss = [int(start_rev)]
    change = []
    inc_val_origin = 0
    dec_val_origin = 0
    count_inc = 0
    count_dec = 0
    inc_date = "0"
    dec_date = "0"


    for row in budget_data:

        # Calculate number of rows and net change
        num_rows += 1
        total += int(row[1])

        # Populate lists for financial record and associated dates
        prof_loss.append(int(row[1]))
        dates.append(row[0])
    

    # Calculate changes in Profit/Losses & store values in list
    for a in range(len(prof_loss)):
        change.append(prof_loss[a] - prof_loss[a-1])

        # Use inbuilt function to find max and min values
        greatest_inc = max(change)
        greatest_dec = min(change)

        # Determine raw revenue data associated with records of greatest
        # increase/ decrease in profits
        # Find position of record in the dataset
        if prof_loss[a] - prof_loss[a-1] == greatest_inc:
            inc_val_origin = prof_loss[a]
            count_inc = a

        elif prof_loss[a] - prof_loss[a-1] == greatest_dec:
            dec_val_origin = prof_loss[a]
            count_dec = a

    # Delete first record of list
    change.pop(0)

    # Calculate Average of changes in Profit/Losses in the dataset
    sum_change = sum(change)
    count_change = len(change)
    average = round((sum_change / count_change), 2)
    
    # Find associated dates for greatest increase/ decrease in profits
    # based on position of record within the dataset
    for b in range(len(dates)):
        if b == count_inc:
            inc_date = dates[b]
        elif b == count_dec:
            dec_date = dates[b]

# Print Final Analysis

print(f'Financial Analysis')
print("------------------------------------------------")
print(f'Total Months: {num_rows}') 
print(f'Total: ${total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {inc_date} (${greatest_inc})')
print(f'Greatest Decrease in Profits: {dec_date} (${greatest_dec})')


with open(r'''C:\Users\bisma\python-challenge\PyBank\Analysis\answer.txt''', "w") as file:
    file.write('Financial Analysis\n')
    file.write('------------------------------------------\n')
    file.write(f'Total Months: {num_rows}\n')
    file.write(f'Average Change: ${average}\n')
    file.write(f'Greatest Increase in Profits: {inc_date} (${greatest_inc})\n')
    file.write(f'Greatest Decrease in Profits: {dec_date} (${greatest_dec})\n')
    file.close