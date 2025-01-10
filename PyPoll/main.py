# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}

# Define lists and dictionaries to track candidate names and vote counts
election_results = {}
candidate_info = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        #Total number of votes cast
        total_votes += 1 

        #Look for unique values in the Candidate column. If the value is unique, add to the dictonary
        if row[2] not in candidate_votes:
                candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

    #Loop through the rows and find the candidate witht he highet number of votes. Write that candidate's name to variable winning_candidate
    for candidate, votes in candidate_votes.items():
        if votes > winning_count:
             winning_count = votes
             winning_candidate = candidate
        
        #calculate the percent of votes each candidate received
        percent_vote = (candidate_votes[candidate] / total_votes )*100
        
        #read the dictionary created above and create a list from the data
        candidate_info.append(candidate)
        candidate_info.append(f"{percent_vote:.03f}%")
        candidate_info.append(votes)
        
    #create variables to hold data for each candidate  
    candidate_1 = (f"{candidate_info[0]}: {candidate_info[1]} ({candidate_info[2]})")
    candidate_2 = (f"{candidate_info[3]}: {candidate_info[4]} ({candidate_info[5]})")
    candidate_3 = (f"{candidate_info[6]}: {candidate_info[7]} ({candidate_info[8]})")


    #create variable output to contain the summary data
    output = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    {candidate_1}
    {candidate_2}
    {candidate_3}
    -------------------------
    Winner: {winning_candidate}
    -------------------------"""

print(output)

# Write the results to a text file
with open(file_to_output, "w") as text_file:
     text_file.write(output)
