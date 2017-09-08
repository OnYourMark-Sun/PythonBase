from datetime import datetime,timedelta,timezone
now = datetime.now()
thiw = datetime.fromtimestamp(84668523521)
print(now-thiw)

print(now+timedelta(days=14))