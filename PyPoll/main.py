import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "election_results.txt")

vote_count = 0
cand_list = []
cand_votes = {}
ballot_count = 0
winner = ""

with open(election_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        vote_count +=  1
        candidate = row[2]

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
    
    for candidate in cand_votes:
        cand_total = cand_votes[candidate]
        percent_votes = float(cand_total)/float(vote_count)*100
        if (cand_total > ballot_count):
            ballot_count = cand_total
            winner = candidate
        print(f"{candidate}: {percent_votes:.3f}% ({cand_total - 1})")
        file.write(f"{candidate}: {percent_votes:.3f}% ({cand_total - 1})\n")
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")  
    
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")