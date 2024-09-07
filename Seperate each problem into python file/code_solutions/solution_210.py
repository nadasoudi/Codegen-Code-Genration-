import arrow

# create a new Arrow object
new_arrow = arrow.Arrow(arrow.now())

# create a new timeframe
new_timeframe = arrow.TimeFrame(new_arrow.floor, new_arrow.hour, new_arrow.minute)

# create a new arrow object
new_arrow = arrow.Arrow(arrow.