import os
import csv

profitLosses={}
total_months=0
profit_losses=0

# importing the csv as read file
Bank_df=os.path.join("resources","budget_data.csv")
with open(Bank_df,'r') as csvfile:
    Bank_info=csv.reader(csvfile, delimiter=",")
    csv_header=next(Bank_info)
    #print(f"CVS Header:{csv_header}")
    for row in Bank_info:
        #print(row)

#The total number of months included in the dataset
        total_months+=1
#The net total amount of "Profit/Losses" over the entire period
       

#The net total amount of "Profit/Losses" over the entire period
        

print(f"""Financial Analysis
----------------------------
Total Months:{total_months}
Total: {profit_losses}""")   



    
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
 

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

# Set variable for output file

#output_file = os.path.join("banking_results.txt""")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = txt.writer(datafile)
       # print(Bank_df)



