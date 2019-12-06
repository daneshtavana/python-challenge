# import required packages
# os module will allow us to create file paths across operating systems
# csv module for reading CSV files
# sys module for printig to external file 
import os
import csv
import sys

# save current state of standard output (print-to-terminal)
orig_stdout = sys.stdout

# set repo_path to repository location
# repo_path = "C:/Users/DaneshT480/MyGithub"
repo_path ="."

# set CSV input file path, specifiy ...
# ... repo_path, repo_name, the sub-directories containing input file
# file_to_load = os.path.join(repo_path,"python-challenge/PyBank","budget_data.csv")
file_to_load = os.path.join(repo_path,"budget_data.csv")

# initialize the main variables 
row_count = 0
months = 0
net_profit = 0
new_profit = 0
old_profit = 0
change_in_profit = 0
sum_change_in_profit = 0
average_profit = 0
max_change_in_profit = 0
min_change_in_profit = 0

# open file_to_load with csv reader, for each row calculate results 
with open(file_to_load, newline='') as budget_data:
    reader = csv.reader(budget_data, delimiter=',')
    
    # Read or skip the header row, then parse each row after the header.  
    header = next(reader)
        
    for row in reader:
        new_profit = int(row[1])
        # two rows are needed to calculate change in profict 
        if row_count == 0:
            change_in_profit = 0
        else:
            change_in_profit = new_profit - old_profit
        # keep track of net_profit by accumulating each row    
        net_profit += new_profit
        # Add each changes in profit, divide by number of rows to get average 
        sum_change_in_profit = sum_change_in_profit + change_in_profit
        # Store maximum amd minimum profit amount and date
        if change_in_profit > max_change_in_profit:
            max_change_in_profit = change_in_profit
            max_profit_date = row[0]
        if change_in_profit < min_change_in_profit:
            min_change_in_profit = change_in_profit
            min_profit_date = row[0]        
        old_profit = new_profit
        row_count +=1   
        
months = row_count
average_profit = sum_change_in_profit/months

# created print function in order to modularize print to terminal or to file 
def print_function():
    print(f"------------------------------------------------")     
    print(f"Financial Analysis Results")        
    print(f"------------------------------------------------")        
    print(f"Total Months: {months} ")
    # format values as currency type 
    print(f"Net profit over entire period: {'${:,.0f}'.format(net_profit)}")
    print(f"Average Change: {'${:,.2f}'.format(average_profit)}")
    print(f"Greatest Increase in profits: {'${:,.0f}'.format(max_change_in_profit)} on {max_profit_date}")   
    print(f"Greatest Decrease in profits: {'${:,.0f}'.format(min_change_in_profit)} on {min_profit_date}") 
   
# invoke print function in order to print to terminal  
print_function()

# change standard output (print-to-file)
# invoke print function in order to print to file  
sys.stdout = open("Financial_Analysis.txt", "w")
print_function()

# close file and reinstate the original stadard output 
sys.stdout.close()
sys.stdout = orig_stdout


