import datetime
current_folder="/home/marie/Bureau/mt-archive/"

def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time lapse in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

now=datetime.datetime.now()
now=roundTime(now,roundTo=15*60)
print(now)
expect=now+datetime.timedelta(hours=-1)
expect=roundTime(expect,roundTo=15*60)
date_time=expect.strftime("%d/%m/%Y,%Hh%M-"+now.strftime("%Hh%M"))
min=now-expect
min=str(int(min.seconds/60))
print()

row=date_time+","+min+",Coding and quality control"
with open(current_folder+"timetrack.csv", "a") as f:


   f.write(row+"\n")
   f.close()