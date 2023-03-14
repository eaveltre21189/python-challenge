# Import modules
import os
import csv

# Define input and output file paths
election_csv = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "election_results.txt")

# Define variables
vote_count = 0
cand_list = []
cand_votes = {}
ballot_count = 0
winner = ""

# Open and read csv file
with open(election_csv) as csv_file:    
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    
    # Loop through rows in csv file
    for row in csv_reader:
        vote_count +=  1
        candidate = row[2]

        # Create candidate list
        if candidate not in cand_list:
            cand_list.append(candidate)
            cand_votes[candidate] = 1
        cand_votes[candidate] = cand_votes[candidate] + 1

# Write data analysis to terminal new text file
with open(output_path, 'w') as file:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(vote_count)}")
    print("-------------------------")
    
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {str(vote_count)}\n")
    file.write("-------------------------\n")
    
    # Calculate count and percentage of votes per candidate; determine winner
    for candidate in cand_votes:
        cand_total = cand_votes[candidate]
        percent_votes = float(cand_total)/float(vote_count)*100
        if (cand_total > ballot_count):
            ballot_count = cand_total
            winner = candidate
        
        # Print candidate data and winner to terminal/output file
        print(f"{candidate}: {percent_votes:.3f}% ({cand_total - 1})")
        file.write(f"{candidate}: {percent_votes:.3f}% ({cand_total - 1})\n")
    
    # Continue printing/writing to output file
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")  
    
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")