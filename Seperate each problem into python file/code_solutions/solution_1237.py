import datetime

class Arrow:
    def __init__(self, hour, minute, second, microsecond):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
    def __str__(self):
        return 'Arrow(%d, %d, %d, %d)' % (self.hour, self.minute, self.second, self.microsecond)