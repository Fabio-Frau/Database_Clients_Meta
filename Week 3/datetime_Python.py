import datetime as dt

current_time = dt.datetime.now()
print(current_time)
print(current_time.date())
print(current_time.time())

week = dt.timedelta(days = 7)
print(current_time.date() + week)


