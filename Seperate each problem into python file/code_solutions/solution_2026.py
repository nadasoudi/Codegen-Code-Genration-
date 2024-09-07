import datetime

def solution(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    start_time = start.strftime('%H:%M:%S')
    end_time = end.strftime('%H:%M:%S')