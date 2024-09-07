import datetime

def time_format(hour, minute, second):
    return f'{hour:02d}:{minute:02d}:{second:02d}'

def main():
    hour = int(input("Enter the hour: "))
    minute = int(input("Enter the minute: "))
    second = int(input("Enter the second: "))
    print(