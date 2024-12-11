from datetime import datetime, timedelta
import calendar

now = datetime.now()

#future and pervious time
future_time = now + timedelta(days=2)
past_time = now - timedelta(weeks=3)

print(future_time.date())
print(past_time.date())

if future_time > past_time:
    print('future date is bigger than previous date')

cal = calendar.month(2025, 1)
print(cal)



## weekday find the weekday of a certain date
cal2 = calendar.weekday(2025, 6, 28)
print(cal2)

## check leap year
print(calendar.isleap(1999))
