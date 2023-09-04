print("Type when your exam is going to start (24 hour format and without colon.)")
print("Also without spaces.")
timeofexam=int(input("Type here."))
print("Type when student arrived. (24 hour format and without colon.)")
print("Also without spaces.")
arrivaltime=int(input("Type here."))
timediff=timeofexam-arrivaltime
if timediff<0:
  print("Late.")
elif timediff<=30 or timediff==0:
  print("On time.")
else:
  print("Too Early.")
print("This is the difference of time between the arrival and the exam time.")
print(timediff," The thousand's and hundred's place show the hours.")
print("The tens and ones place will show the minutes.")