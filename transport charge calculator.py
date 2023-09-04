km=float(input("Type the number of kilometers you are going to travel."))
time=(input("What period of the day do you want to travel.(Day or Night)"))
#train
traincost=round(km*0.06)
print("Cost for train in USD (Rounded):",traincost)
#Bus
buscost=round(km*0.09)
print("Cost for bus in USD (Rounded):",buscost)
#taxi  
if time=="Day":
  taxicost=round(km*0.79)+0.70
  print("Cost for taxi in USD (Rounded):",taxicost)
else:
  taxicost=round(km*0.90)+0.70
  print("Cost for taxi in USD (Rounded):",taxicost)