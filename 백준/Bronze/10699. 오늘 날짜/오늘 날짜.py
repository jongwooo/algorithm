import datetime

tz = datetime.timezone(datetime.timedelta(hours=9))
print(datetime.datetime.now(tz=tz).strftime("%Y-%m-%d"))
