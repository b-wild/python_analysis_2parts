import os
import csv

canidate_votes={}
total_votes=0
winner_vote=0
winner_name=""

# importing the csv as read file
Election_df=os.path.join("resources","election_data.csv")
with open(Election_df) as csvfile:
    Election_results=csv.reader(csvfile, delimiter=",")
    csv_header=next(Election_results)
    for row in Election_results:
        #print(row)

# The total number of votes cast
        total_votes+=1
        if row[2] in canidate_votes:
            canidate_votes[row[2]]+=1
        else:
            canidate_votes[row[2]]=1

#print(canidate_votes)  
print(f"""Election Results
--------------------------
Total Votes: {total_votes}
--------------------------""")          
    
# A complete list of candidates who received votes
for canidate in canidate_votes:
    print(f"{canidate} {canidate_votes[canidate]/total_votes *100} ( {canidate_votes[canidate]} )")
    #print(f"Votes for canidate: {canidate_votes[canidate]}")
    #print(f"percentage: {canidate_votes[canidate]/total_votes *100}")
    #print("----------------------")
    if winner_vote < canidate_votes[canidate]:
        winner_vote=canidate_votes[canidate]
        winner_name=canidate

print(f"""----------------------
Name: {winner_name}
-----------------""")
 
#  Set variable for output file
#output_file = os.path.join("Election_results.txt")


#  Open the output file
#with open(output_file, "w") as datafile:
 #   writer = txt.writer(datafile)
  #     print(Election_df)