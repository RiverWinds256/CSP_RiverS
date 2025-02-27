# river Stanley, time of day python 
import time
print("Welcome")
first_time= time.gmtime()
current= time.time()
now= time.ctime(current)
localtime = time.localtime(current)
day = localtime.tm_wday
hour = localtime.tm_hour 

if hour<12:
    print("good morning")
elif 12<=hour<18:
    print("good afternoon")
else:
    print("good evening")    