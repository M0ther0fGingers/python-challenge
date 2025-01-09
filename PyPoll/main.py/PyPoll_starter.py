# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}

# Define lists and dictionaries to track candidate names and vote counts
#candidate_name = {"ccs": "Charles Casper Stockham", "dg": "Diana DeGette", "rad": "Raymon Anthony Doane"}
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

    #Loop through the rows and find the candidate witht he highet number of votes
    for candidate, votes in candidate_votes.items():
        if votes > winning_count:
             winning_count = votes
             winning_candidate = candidate
        #calculate the percent of votes each candidate received
        percent_vote = (candidate_votes[candidate] / total_votes )*100
        #read the dictionary and create a list of the data 
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
    -------------------------)"""

print(output)




        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


        # Generate and print the winning candidate summary


        # Save the winning candidate summary to the text file