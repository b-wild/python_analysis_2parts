import os
import csv

profit_losses={}
profit=0
total_months=0


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
    for row[0] in profit_losses:
        profit_losses[row[0]]
                   


    
print(f"""Financial Analysis
----------------------------
Total Months:{total_months}
Total: {profit_losses}""")

#the net total amount of "Profit/Losses" over the entire period
        
  
    
#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

# Set variable for output file

#output_file = os.path.join("banking_results.txt""")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = txt.writer(datafile)
       # print(Bank_df)



