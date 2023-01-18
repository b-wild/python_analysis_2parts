import os
import csv

total_profit=0
total_months=0
change_month=[]
change_profit_losses=[]
profit_loss_change=0
previous_change=0
increase=0
decrease=999999999999999
index=0


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
#The changes in "Profit/Losses" over the entire period, and then the average of those change        
if profit_loss_change not in change_profit_losses:
    change_month = change_month + [row[0]]
    previous_change = int(row[1])
    profit_loss_change = int(row[1]) - previous_change
    change_profit_losses.append(profit_loss_change)
else:
    previous_change = int(row[1])
    change_month = change_month + [row[0]]

decrease = min(change_profit_losses) 
increase = max(change_profit_losses)
 #add 1 because month associated with change is the second month
Decrease_month = change_profit_losses.index(decrease)-1
Increase_month = change_profit_losses.index(increase)-1

    
print(f"""Financial Analysis
----------------------------
Total Months:{total_months}
Total: ${total_profit}
Average Change: ${round(sum(change_profit_losses)/len(change_profit_losses),2)}
Greatest Increase in Profits: {change_month[Increase_month]} (${increase})
Greatest Decrease in Profits: {change_month[Decrease_month]} (${decrease})
----------------------------""")
 

output_file = os.path.join("analysis", "Bank_results.txt")

#   Open the output file
with open(output_file, "w") as output:
   output.write("""Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
----------------------------""")



