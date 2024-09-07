import datetime

def solution(files):
    answer = []
    for file in files:
        with open(file, 'r') as f:
            date = f.readline().split()
            time = f.readline().split()
            date = datetime.datetime.strptime(date[0], '%Y-%m-%d %H:%M:%S')
            time = datetime.datetime.strptime(time[0], '%H:%M: