import os
import csv
# importing the csv as read file
Bank_df=os.path.join("resources","budget_data.csv")
with open(Bank_df,'r') as csvfile:
    Bank_info=csv.reader(csvfile, delimiter=",")
    csv_header=next(Bank_info)
    print(f"CVS Header:{csv_header}")
    for row in Bank_info:
        #print(row)

#The total number of months included in the dataset
        month_total=()
        for row in Bank_info:
            months=row(0)
            month_total.append(months)
            print(len(month_total))


#The net total amount of "Profit/Losses" over the entire period
        #gainLosses =()
        #for row in Bank_info:
         #   gain_loses=(row(1+1)-row(1))
          #  gainLosses.append(gain_loses)
           # print(gainLosses)



#The changes in "Profit/Losses" over the entire period, and then the average of those changes
        #change_profit =sum(gainLosses)
            #print(f"Profit/Losses over entire period = {change_profit})
        #percent_change=(change_profit/len(gainLosses)*100)
            #print(f"Percent change over entire period = {percent_change})

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period


# Set variable for output file
print(f"""Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: {change_profit}
  Average Change: {percent_change}
  Greatest Increase in Profits: {greatest_increase}
  Greatest Decrease in Profits: {greatest+decr3ease}""")
  
#output_file = os.path.join("banking_results.txt""")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = txt.writer(datafile)
       # print(Bank_df)



