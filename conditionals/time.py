# river Stanley, how to get time of day
import time

#find first instance of time in programing
first_time= time.gmtime()
#print(first_time)

#current time in seconds 
current= time.time()
#print(current) #senonds since jan 1st 1970

#current date and time like we see it normally
now= time.ctime(current)
#print(now)

#just get a part of the time 
localtime = time.localtime(current)
day = localtime.tm_wday
hour = localtime.tm_hour #in military time  (0-23)
print(hour)