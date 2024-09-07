import datetime

class Arrow:
    def __init__(self, hour, minute, second, microsecond, timestamp):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.timestamp = timestamp
    
    def __str__(self):
        return f'{self.hour}:{self.minute}:{self