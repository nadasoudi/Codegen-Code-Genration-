import arrow

def check_date(date):
    if arrow.get(date).time() >= arrow.get(date).time():
        return True
    else:
        return False

print(check_date("2021-05-01"))
print(check_date("2021-05-02"))
print(check_date("2021-05-03"))
print(check_date("2021-05-04"))
print(check_date