import csv

# Set the path for file
csvpath="Resources/budget_data.csv"


# Creating this variable to loop through each row
month_count=0
total_profit=0

# calculating the changes
changes= []
# to find the last month profit 
last_month_profit = None
month_changes=[]

# Open the CSV using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

    # Count months
        month_count=month_count+1

    # add profit
        total_profit=total_profit + int(row[1])

    # need last month profit
    # subract this month minus last month
    # APPEND that change to the list
    
    # IF first row, there is no change
        if (month_count == 1):
            # this is the FIRST row
            # no change
            last_month_profit=int(row[1])
        else:
            change=int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])
        
             # Reset
            last_month_profit=int(row[1])

 
    print("Financial Analysis\n")
    print(f"Total Months: {month_count} ")
    print(f"Total: ${total_profit} ")


    avg_change = sum(changes) / len(changes)
    print(f"Average Change: ${avg_change:.2f} ")

    max_change=max(changes)
    max_month_indx=changes.index(max_change)
    max_month = month_changes[max_month_indx]

   
    print(f"Greatest Increase in Profits: {max_month} (${max_change}) ")
    min_change=min(changes)
    min_month_indx=changes.index(min_change)
    min_month = month_changes[min_month_indx]
    
   
    print(f"Greatest Decrease in Profits: {min_month} (${min_change}) ")


# Export the output to a txt File
textpath = "analysis/analysis.txt"
with open(textpath, 'w') as analysis:
    analysis.write("Financial Analysis\n\n")
    analysis.write(f"Total Months: {month_count}\n")
    analysis.write(f"Total: ${total_profit}\n")
    analysis.write(f"Average Change: ${avg_change:.2f}\n")
    analysis.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    analysis.write(f"Greatest Decrease in Profits: {min_month} (${min_change})\n")