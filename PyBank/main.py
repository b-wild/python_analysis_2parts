import os
import csv

profit_losses=[]
total_profit=0
total_loss=0
profit=0
total_months=0
increase_date=""
decrease_date=""



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
        total_profit = total_profit+ int(row[1])




        #if profit < profit_losses:
         #   profit=profit_losses
            #increase_date=

    
print(f"""Financial Analysis
----------------------------
Total Months:{total_months}
Total: ${total_profit}""")

#the net total amount of "Profit/Losses" over the entire period
        
  
    
#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#output_file = os.path.join("analysis", "Bank_results.txt")

#   Open the output file
#with open(output_file, "w") as output:
 #   output.write("""Financial Analysis
 # ----------------------------
 # Total Months: 86
 # Total: $22564198
 # Average Change: $-8311.11
 # Greatest Increase in Profits: Aug-16 ($1862002)
 # Greatest Decrease in Profits: Feb-14 ($-1825558)
 # ```""")



