hour1 = datetime.datetime.strptime('10:00', '%H:%M')
hour2 = datetime.datetime.strptime('10:30', '%H:%M')

print(hour1.strftime('%H:%M'))
print(hour2.strftime('%H:%M'))

# Solution:

# hour1 = datetime.datetime.strptime('10:00', '%H:%M')