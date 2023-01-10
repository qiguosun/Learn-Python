from datetime import datetime, timedelta
from datetime import datetime
import time

print(time.time())


def send_emails():
    for i in range(500000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = start-end
print(duration)


################ datetime object ####################
dt = datetime(2018, 1, 1)
print(dt)
print(datetime.now())

dt = datetime.strptime("2019/01/01", "%Y/%m/%d")
print(dt)
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

################## time Deltas ########################

dt1 = datetime(2019, 1, 1) + timedelta(1)
print(dt1)
dt2 = datetime.now()

duration = dt2-dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total-seconds", duration.total_seconds())
