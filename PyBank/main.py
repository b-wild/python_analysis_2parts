import os
import csv
# importing the csv as read file
Bank_df=os.path.join("resources","budget_data.csv")
with open(Bank_df) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    print(f"CVS Header:{csv_header}")
    for row in csvreader:
        print(row)
# determing the number of months
    Bank_df.len(0)




