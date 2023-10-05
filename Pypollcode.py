
import os
import csv

# Lists to store data
total_votes = 0



csvpath = os.path.join('..','PyPoll/Resources','election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    for poll_data in csvreader:
        total_votes = total_votes + 1







        print("Total Votes", total_votes)