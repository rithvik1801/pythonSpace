month=str(input("Enter a month"))
day=int(input("Enter a day"))

if (day<=0 or day>31):
  print("Not a valid day")
elif ((month=="January" or month=="1" or month=="01") and day>31) or ((month=="February" or month=="2" or month=="02") and day>29) or ((month=="March" or month=="3" or month=="03") and day>31) or ((month=="April" or month=="4" or month=="04") and day>30) or ((month=="May" or month=="5" or month=="05") and day>31) or ((month=="June" or month=="6" or month=="06") and day>30) or ((month=="July" or month=="7" or month=="07") and day>31) or ((month=="August" or month=="8" or month=="08") and day>31) or ((month=="September" or month=="9" or month=="09") and day>30) or ((month=="October" or month=="10") and day>31) or ((month=="November" or month=="11") and day>30) or ((month=="December" or month=="12") and day>31):
  print("Not a valid date")
elif (month=="March" or month=="3" or month=="03")  or (month=="April" or month=="4" or month=="04")  or (month=="May" or month=="5" or month=="05"): 
  print("Spring")
elif (month=="June" or month=="6" or month=="06") or (month=="July" or month=="7" or month=="07") or (month=="August" or month=="8" or month=="08"):
  print("Summer")
elif (month=="September" or month=="9" or month=="09") or (month=="October" or month=="10") or (month=="November" or month=="11"):
  print("Autumn")
elif (month=="December" or month=="12") or (month=="January" or month=="1" or month=="01") or (month=="February" or month=="2" or month=="02"):
  print("Winter")