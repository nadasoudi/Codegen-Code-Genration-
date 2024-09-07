import datetime

def iso_week_number(iso_year, iso_week):
    iso_week_number = datetime.datetime(iso_year, 1, 1).isocalendar()[1]
    return iso_week_number

def iso_weekday(iso_year, iso_week):
    iso_weekday = datetime.datetime(iso_year, 1, 1).