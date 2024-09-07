python sol_python.py

"""

# import the necessary packages
from datetime import date
import calendar
import calendar as c
import datetime

# define a function to select all the Sundays of a specified year
def select_sundays(year):
    # create a list of the calendar days of the specified year
    calendar_days = c.Calendar().itermonthdays(year, 1)
    # create a list of the calendar days of the specified year
    calendar_days