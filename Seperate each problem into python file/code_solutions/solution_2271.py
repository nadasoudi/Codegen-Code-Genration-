def divide_date_range(start_date, end_date, duration):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    duration = int(duration)
    start_date = start_date + timedelta(days=duration)
    end_date = end_date + timedelta(days=duration)
    return