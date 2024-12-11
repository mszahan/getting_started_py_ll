##datetime module
from datetime import datetime

now = datetime.now()

print(now.date())
print('year', now.year)
print('month', now.month)
print('hour', now.hour)
print(now.minute)
print(now.second)
print(now.time())
