import os
import csv
# importing the csv as read file
Election_df=os.path.join("resources","election_data.csv")
with open(Election_df) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #print(row)

# The total number of votes cast
       
# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# Set variable for output file
#output_file = os.path.join("banking_results.txt")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = txt.writer(datafile)
       # print(Election_df)