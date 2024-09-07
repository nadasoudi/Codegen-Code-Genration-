import datetime

def convert_unix_to_utc(unix_time):
    """
    Converts unix time to UTC timezone
    """
    utc_time = datetime.datetime.utcfromtimestamp(unix_time)
    return utc_time.strftime('%Y-%m-%d %H:%M:%S')

def convert