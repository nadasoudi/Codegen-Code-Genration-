import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_votes = 0
    candidate_votes = {}
    candidate_votes_list = []
    candidate_votes_percentage = {}
    candidate_votes_percentage