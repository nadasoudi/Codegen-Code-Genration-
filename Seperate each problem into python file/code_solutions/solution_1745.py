import random

def generate_dates(start, end, k):
    """
    Generate dates between two other dates
    """
    dates = []
    for i in range(k):
        date = random.randint(start, end)
        dates.append(date)
    return dates

def main():
    """
    Main function to generate dates between two other dates
    """
    start = int(input("Enter the start date: "))
    end = int(input("