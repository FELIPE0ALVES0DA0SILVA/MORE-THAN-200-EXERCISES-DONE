import datetime
import pytz

today = datetime.date.today()
# print(today)
# print(today.weekday())
# print(today.isoweekday())

# tdelta = datetime.timedelta(days=7)
# print(today - tdelta)

# bday = datetime.date(2020, 10, 21)

# till_bday = bday - today
# print(till_bday.days)

# T = datetime.time()
# print(T)

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone("America/Sao_Paulo"))
print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)
