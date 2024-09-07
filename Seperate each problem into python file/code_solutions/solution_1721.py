import datetime

def group_dates(start, end, k):
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
    for i in range(k):
        yield start_date + datetime.timedelta(days=i)

print(list(group_dates('2021-01-01', '