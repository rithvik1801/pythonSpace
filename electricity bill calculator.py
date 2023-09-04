Units=int(input("Type the number of Units used."))
if Units<=100:
  cost=0
  print("Rs.",cost)
elif Units>100 and Units<300:
  cost=(Units-100)*2
  print("Rs.",cost)
elif Units>300 and Units<600:
  cost=(200*2)+(Units-300)*3
  print("Rs.",cost)
else:
  cost=(200*2)+(300*3)+(Units-600)*5
  print("Rs.",cost)  