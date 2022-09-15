def add_time(start, duration, dayofweek):

  index=None
  
  if dayofweek=="Monday":
    index=1
  elif dayofweek=="Tuesday":
    index=2
  elif dayofweek=="Wednesday":
    index=3
  elif dayofweek=="Thursday":
    index=4
  elif dayofweek=="Friday":
    index=5
  elif dayofweek=="Saturday":
    index=6
  elif dayofweek=="Sunday":
    index=7

  start_tup=start.partition(":")
  start_hours=start_tup[0]
  start_mins=start_tup[2].split()[0]
 
  
  duration_tup=duration.partition(":")
  duration_hours=duration_tup[0]
  duration_mins=duration_tup[2]

  new_hour=int(start_hours)+int(duration_hours)
  new_min=int(start_mins)+int(duration_mins)
 
  if new_min > 60:
    addhour=new_min//60
    remain=new_min%60
    new_hour+=addhour
    new_min=remain

  ampm=start_tup[2].split()[1]
  am_or_pm={"AM":"PM", "PM":"AM"}

  days=0
  
  while new_hour > 24:
    new_hour-=24
    days+=1

  new_days= " (" +str(days) +" days later)"

  cycle = (int(start_hours) + int(duration_hours))/12

  if cycle % 1 == 0:
    ampm=am_or_pm[ampm]
  else:
    pass
    
  if new_hour > 12:
    new_hour-=12
  
  if new_min < 10:
    new_min = "0"+str(new_min)

  index=index+int(days)
  if index > 7:
    index=index%7
    
  if index == 1:
    dayofweek="Monday"
  if index == 2:
    dayofweek="Tuesday"
  if index == 3:
    dayofweek="Wednesday"
  if index == 4:
    dayofweek="Thursday"
  if index == 5:
    dayofweek="Friday"
  if index == 6:
    dayofweek="Saturday"
  if index == 7:
    dayofweek="Sunday"


  new_time = str(new_hour) +":" +str(new_min) + " "+ ampm + new_days
  
  if (dayofweek):
    new_time = str(new_hour) +":" +str(new_min) + " "+ ampm + ", " + dayofweek + new_days


  return new_time

print(add_time("12:59 AM", "84:00", "Sunday"))
