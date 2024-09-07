def timezone_convert(tz_str, utc_str, local_str):
    if tz_str == "UTC":
        utc_str = utc_str.replace("+00:00", "")
        utc_str = utc_str.replace("-00:00", "")
        utc_str = utc_str.replace("+00:00", "")
        utc_str = utc_str