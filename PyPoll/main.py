# Import OS Module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(r'''C:\Users\bisma\python-challenge\PyPoll\Resources\election_data.csv''')

# Read using CSV module
with open(csvpath) as csvfile:

    poll_data = csv.reader(csvfile, delimiter = ',')

    # Read the header row first
    csv_header = next(poll_data)

    # Declare global variables
    num_votes = 0
    candidates_list = []
    candidates_unique = []
    cand_0_name = ""
    cand_1_name = ""
    cand_2_name = ""
    cand_3_name = ""
    cand_0_count = 0
    cand_1_count = 0
    cand_2_count = 0
    cand_3_count = 0
    cand_0_per = 0.0
    cand_1_per = 0.0
    cand_2_per = 0.0
    cand_3_per = 0.0
    winner = ""

    # Calculate total number of votes cast and for whom in the election
    for row in poll_data:
        num_votes +=1
        candidates_list.append(row[2])
    
    # Compile list of unique candidate names
    for name in candidates_list:
        if name not in candidates_unique:
            candidates_unique.append(name)

    # Assign each unique value to a candidate name
    cand_0_name = candidates_unique[0]
    cand_1_name = candidates_unique[1]
    cand_2_name = candidates_unique[2]
    cand_3_name = candidates_unique[3]

    # Count number of votes cast for each candidate
    for candidate in candidates_list:
        if candidate == candidates_unique[0]:
            cand_0_count += 1
        elif candidate == candidates_unique[1]:
            cand_1_count += 1
        elif candidate == candidates_unique[2]:
            cand_2_count += 1
        else:
            cand_3_count += 1
    
    # Calculate the percentage of votes received by each candidate
    cand_0_per = '{:.3f}%'.format((cand_0_count/ num_votes) * 100)
    cand_1_per = '{:.3f}%'.format((cand_1_count/ num_votes) * 100)
    cand_2_per = '{:.3f}%'.format((cand_2_count/ num_votes) * 100)
    cand_3_per = '{:.3f}%'.format((cand_3_count/ num_votes) * 100)

    # Determine the winner of the popular vote by comparing total votes per candidate
    if cand_0_count > cand_1_count and cand_0_count > cand_2_count and cand_0_count > cand_3_count:
        winner = cand_0_name
    elif cand_1_count > cand_0_count and cand_1_count > cand_2_count and cand_1_count > cand_3_count:
        winner = cand_1_name
    elif cand_2_count > cand_0_count and cand_2_count > cand_1_count and cand_2_count > cand_3_count:
        winner = cand_2_name
    elif cand_3_count > cand_0_count and cand_3_count > cand_1_count and cand_3_count > cand_2_count:
        winner = cand_3_name

    # Print results to terminal
    print(f'Election Results')
    print('-------------------------------------------------')
    print(f'Total Votes: {num_votes}')
    print('-------------------------------------------------')
    print(f'{cand_0_name}: {cand_0_per} ({cand_0_count})')
    print(f'{cand_1_name}: {cand_1_per} ({cand_1_count})')
    print(f'{cand_2_name}: {cand_2_per} ({cand_2_count})')
    print(f'{cand_3_name}: {cand_3_per} ({cand_3_count})')
    print('-------------------------------------------------')
    print(f'Winner: {winner}')
    print('-------------------------------------------------')

    # Export results to text file
    with open(r'''C:\Users\bisma\python-challenge\PyPoll\Analysis\Election_Analysis.txt''', "w") as file:
        file.write(f'Election Results\n')
        file.write('-------------------------------------------------\n')
        file.write(f'Total Votes: {num_votes}\n')
        file.write('-------------------------------------------------\n')
        file.write(f'{cand_0_name}: {cand_0_per} ({cand_0_count})\n')
        file.write(f'{cand_1_name}: {cand_1_per} ({cand_1_count})\n')
        file.write(f'{cand_2_name}: {cand_2_per} ({cand_2_count})\n')
        file.write(f'{cand_3_name}: {cand_3_per} ({cand_3_count})\n')
        file.write('-------------------------------------------------\n')
        file.write(f'Winner: {winner}\n')
        file.write('-------------------------------------------------\n')
        file.close
