import datetime

def get_timestamp():
    return datetime.datetime.now()

def get_datetime():
    return datetime.datetime.now()

def get_timestamp_as_string():
    return get_timestamp().strftime('%Y-%m-%d %H:%M:%S')

def get_datetime_as_string():
    return get_datetime().strftime('%Y-%m-