import datetime

def add_time(start, duration):
    """
    :type start: datetime.datetime
    :type duration: datetime.timedelta
    :rtype: datetime.datetime
    """
    start_time = start.strftime("%H:%M")
    end_time = start + duration
    return end_time

# driver code
start = datetime.datetime.now()
duration = datetime.timedelta(hours=1, minutes