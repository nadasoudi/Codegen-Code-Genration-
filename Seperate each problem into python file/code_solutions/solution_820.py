import datetime

def get_day_after(date):
    return date.day

def get_day_before(date):
    return date.day - 1

def get_days_between(date1, date2):
    return (date2 - date1).days

def main():
    date1 = datetime.date(2021, 1, 1)
    date2 = datetime.date(2021, 1,