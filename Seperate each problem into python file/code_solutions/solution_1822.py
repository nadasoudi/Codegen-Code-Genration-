import csv
import os

def csv_to_pdf(csv_file):
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            pdf_file = row[0] + '.pdf'
            pdf_file = pdf_file.replace(' ', '_')
            pdf_file = pdf_file.replace('.csv