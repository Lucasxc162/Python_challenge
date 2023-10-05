
import csv
import os

# Lists to store data
total_months = 0
net_amount = 0
average_change = 0
increase_greatest = [" ",0]
decrease_greatest = [" ",0]
current_amount = 0
previous_amount= 0
change = 0
total_change = 0

# Empty list for change
change_list = []

# Reach file
csvpath = os.path.join("..","PyBank/Resources","budget_data.csv")

# Open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header of file
    csv_header = next(csvreader)
    
    for bank_data in csvreader:
        current_amount = int(bank_data[1])
        change = current_amount - previous_amount
        previous_amount = current_amount
        total_change += change
        change_list += [change]
        net_amount = net_amount + int(bank_data[1])
        total_months = total_months + 1
        average_change = change / total_months
        if change > increase_greatest[1]:
            increase_greatest[0] = bank_data[0]
            increase_greatest[1] = change
        if change < decrease_greatest[1]:
            decrease_greatest[0] = bank_data[0]
            decrease_greatest[1] = change   


    print("Total Months", total_months)
    print("Total Profits/Losses: $", net_amount)
    print("Average Change in Profits/Losses: $", average_change)  
    print("Greatest Increase: $", increase_greatest)
    print("Greatest Decrease: $", decrease_greatest)

        

    