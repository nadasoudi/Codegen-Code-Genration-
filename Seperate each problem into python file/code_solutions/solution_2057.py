python solution.py

"""

import json
import csv
import os

def main():
    """
    Main function to run the program
    """
    # Get the path to the directory containing the JSON files
    directory = os.path.dirname(os.path.abspath(__file__))
    # Get the path to the directory containing the CSV files
    directory = os.path.join(directory, "csv")
    # Create the CSV files
    csv_files = [os.path.join