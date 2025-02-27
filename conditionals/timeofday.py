# river Stanley, time of day python 
import time

first_time= time.gmtime()
current= time.time()
now= time.ctime(current)
localtime = time.localtime(current)
day = localtime.tm_wday
hour = localtime.tm_hour 
