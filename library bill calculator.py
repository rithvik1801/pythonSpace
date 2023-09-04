days=int(input("Type the number of days you borrowed your book from the library."))
if days<=5:
  cost=days*2
  print("Rs.",cost)
elif days>=6 and days<=10:
  cost=(5*2)+(days-5)*3
  print("Rs.",cost)
elif days>=11 and days<=15:
  cost=(5*2)+(5*3)+(days-10)*4
  print("Rs.",cost)
else:
  cost=(5*2)+(5*3)+(5*4)+(days-15)*5
  print("Rs.",cost)  