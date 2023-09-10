import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Initialize variables to store vote counts for each candidate
total_votes = 0
candidate_votes = {}

# Open and read the CSV file with UTF-8 encoding
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1

        # Extract the candidate's name from the row
        candidate_name = row[2]

        # Update the vote count for the candidate in the dictionary
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

# Find the winner by identifying the candidate with the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Calculate the percentage of votes for each candidate
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Print the election results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Define the path to the output text file
output_file = os.path.join("Election_Analysis.txt")

# Write the election results to the output text file
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")