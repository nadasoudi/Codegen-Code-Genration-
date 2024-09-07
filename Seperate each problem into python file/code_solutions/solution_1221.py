import arrow

print(arrow.now())
print(arrow.utcnow())
print(arrow.utcnow().isoformat())
print(arrow.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
print(arrow.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(arrow.utcnow().strftime("%Y-%m