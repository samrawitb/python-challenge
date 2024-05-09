import csv

csvpath="Resources/election_data.csv"

# Create variable
vote_count=0

# Create a variable for each candidate
candidateC= 0
candidateD=0
candidateR=0

# Open the CSV using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    # Read in CVS header row
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
        
    for candidates in csvreader:
        vote_count=vote_count+1

        if (candidates[2]=="Charles Casper Stockham"):
            candidateC += 1
        elif (candidates[2] == "Diana DeGette"):
            candidateD += 1
        else:
            candidateR += 1


    print(f"Vote Count: {vote_count}")
    print(f"Total number of votes for Charles Casper Stockham: {candidateC}")
    print(f"Total number of votes for Diana DeGette: {candidateD}")
    print(f"Total number of votes for Raymon Anthony Doane: {candidateR}")


percentC = candidateC / vote_count * 100
percentD = candidateD / vote_count * 100
percentR = candidateR / vote_count * 100

print(f"Charles Casper Stockham: {percentC:.3f}% ({candidateC})")
print(f"Diana DeGette: {percentD:.3f}% ({candidateD})")
print(f"Raymon Anthony Doane: {percentR:.3f}% ({candidateR})")

winner = ""

if (percentC > percentD) and (percentC > percentR):
    winner = "Charles Casper Stockham"

elif (percentD > percentC) and (percentD > percentR):
    winner = "Diana DeGette"

else:
     winner= "Raymon Anthony Doane"

print(f"Winner: {winner}")

# Export the output to a txt file
textpath = "analysis/analysis.txt"
with open(textpath, 'w') as analysis:
    analysis.write("Election Results\n\n")
    analysis.write(f"Total Votes: {vote_count}\n\n")
    analysis.write(f"Charles Casper Stockham: {percentC:.3f}% ({candidateC})\n")
    analysis.write(f"Diana DeGette: {percentD:.3f}% ({candidateD})\n")
    analysis.write(f"Raymon Anthony Doane: {percentR:.3f}% ({candidateR})\n\n")
    analysis.write(f"Winner: {winner}")
   
