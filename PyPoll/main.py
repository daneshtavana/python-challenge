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
repo_path = "."

# set CSV file: repo_path, repo_name, sub-directories and the CSV file to load
# file_to_load = os.path.join(repo_path,"python-challenge/PyPoll","election_data.csv")
file_to_load = os.path.join(repo_path,"election_data.csv")

# create lists and vaiables for placeholders of contents
candidate_name = []
candidate_vote = []
candidate_rating = 0
total_vote = 0
    
# open the CVS
# reader specifies the delimiter and variable that holds contents
with open(file_to_load, newline='') as election_data:
    reader = csv.reader(election_data, delimiter=',')
    
    # Read or skip the header row, then parse each row after the header.  
    header = next(reader)

    # Loop through each row, grab each field and store in a list
    for row in reader:
        
        # Grab candidate name and store it into list
        if row[2] not in candidate_name:
            candidate_name = candidate_name + [row[2]]
            candidate_vote = candidate_vote + [0]
        index = candidate_name.index(row[2])
        candidate_vote[index] += 1
        total_vote += 1

max_vote = max(candidate_vote)
index = candidate_vote.index(max_vote)
winner = candidate_name[index]

def print_function():
    print(f"Election Results")        
    print(f"-------------------------------------")        
    print(f"Total Votes: {total_vote}")
    print(f"-------------------------------------")                
    for i in range(len(candidate_name)): 
        candidate_rating = candidate_vote[i]/total_vote
        print(f"{candidate_name[i]}: {'{:.3%}'.format(candidate_rating)} ({candidate_vote[i]})")
    print(f"-------------------------------------")        
    print(f"Winner: {winner}")
    print(f"-------------------------------------")           

# invoke print function in order to print to terminal  
print_function()

# change standard output (print-to-file)
# invoke print function in order to print to file  
sys.stdout = open("Election_Results.txt", "w")
print_function()

# close file and reinstate the original stadard output 
sys.stdout.close()
sys.stdout = orig_stdout