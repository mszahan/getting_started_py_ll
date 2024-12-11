from datetime import datetime


now = datetime.now()

## %a - Mon, Tues, Wed
## %A - Monday, Tuesday, Wednesday
## %d - 10th January (10)

print(now.strftime('%a %A %d'))

## %b - Jan, Feb
## %B - January, February
## %m - 01, 02

print(now.strftime('%b %B %m'))

## %H - hours
## %M - minutes
## %S - seconds
## %p - am or pm

print(now.strftime('%H %M %S %p'))

## %y - 24
## %Y - 2024

print(now.strftime('%y %Y'))

