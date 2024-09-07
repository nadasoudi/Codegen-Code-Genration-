def extract_year(date):
    return date.split('-')[0]

def extract_month(date):
    return date.split('-')[1]

def extract_date(date):
    return date.split('-')[2]

def extract_time(date):
    return date.split('-')[3]

def solution(date):
    date = date.split('-')
    return extract_year(date[0]),