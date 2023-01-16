import os
import csv
# importing the csv as read file
Bank_df=os.path.join("resources","budget_data.csv")
with open(Bank_df) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    print(f"CVS Header:{csv_header}")
    for row in csvreader:
        #print(row)
# determing the number of months
    for months in range()
        
    print(f"There are (len(months)) months.")
    
    




# Set variable for output file
#output_file = os.path.join("banking_results.txt")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = txt.writer(datafile)
       # print(Bank_df)



