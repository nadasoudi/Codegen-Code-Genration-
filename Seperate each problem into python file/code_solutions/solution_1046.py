date1 = input("Enter the first date in the format dd/mm/yyyy: ")
date2 = input("Enter the second date in the format dd/mm/yyyy: ")

print("Number of days between", date1, "and", date2, "is",
      calculate_days(date1, date2))

"""

def calculate_days(date1, date2):
    """
    Calculate number of days between two dates.

    :param date1