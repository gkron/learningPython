import time
import calendar

time1 = time.time()
print(time1)  # 1547008876.8666322

# local time
localtime = time.localtime(time.time())
print(localtime)

# o/p:  time.struct_time(tm_year=2019, tm_mon=1, tm_mday=9, tm_hour=10, tm_min=9, tm_sec=26, tm_wday=2, tm_yday=9, tm_isdst=0)

#how to get foramte time

formattime = time.asctime(time.localtime(time.time()))
print(formattime)  # Wed Jan  9 10:11:16 2019

# how to get calender for month

cal = calendar.month(2019,11)
print(cal)
