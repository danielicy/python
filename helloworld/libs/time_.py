import time
from datetime import datetime

print(time.time())
dt = datetime(2021, 1, 1)
dt1 = datetime.now()
dt2 = datetime.strptime("2021/01/01", "%Y/%m/%d")
dt3 = datetime.fromtimestamp(time.time())
print(dt1)
print(dt1.strftime("%Y/%m"))
print(dt3)
