import datetime

def datetime_to_timestamp(dt):
    return int(dt.timestamp())

def timestamp_to_datetime(ts):
    return datetime.datetime.fromtimestamp(ts)

def timestamp_to_datetime_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def timestamp_to_datetime_str_with_tz(ts):