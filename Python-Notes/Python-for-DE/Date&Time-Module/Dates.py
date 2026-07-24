import datetime
import pytz


## printing Date
"""
d = datetime.date(2021,8,8)
print(d)
"""

tday = datetime.date.today()
"""
print(tday)

print()
print('------------')
print()
"""

"""
print(tday.weekday()) # For weekday Monday is 0 and Sunday is 6

print(tday.isoweekday())  # For weekday Monday is 1 and Sunday is 7
"""

## Using Time timedelta

"""
Date2 = Date1 +- timedelta
timedelta = Date1 +- Date2
"""

# tdelta = datetime.timedelta(days=7)

# print("going seven Days before the current date",tday - tdelta)

## Finding The Days Between The Bday and Current Day

bday = datetime.date(2026,8,8)
"""
till_bday = bday - tday
print('Days Before birthday',till_bday.days)
"""


"""
Now We are Using The Time
"""
##              Hour,minutes,sec,microsec
# t = datetime.time(9,3,45,100000)
# print(t.hour)

## We want date also with time then we use (datetime.datetime)

"""
dt = datetime.datetime(2026,7,20,8,23,45,10000)
print(dt.year)

tdelta = datetime.timedelta(hours=18)

print(dt + tdelta)
"""

# We are Using other Key word of Datetime
"""
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
"""

# Now We are Using pytz for Timezone We are using only second code

dt = datetime.datetime(2026,7,20,12,23,45, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_mtz = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
# print(dt_mtz)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)


# Finding Out How Many Timezone There in pytz

# for tz in pytz.all_timezones:
    # print(tz)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('Asia/Kolkata')

dt_mtn = mtn_tz.localize(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('Asia/Kolkata'))
# print(dt_east)

dt_east = dt_mtn.astimezone(pytz.timezone('Asia/Kolkata'))
# print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime
