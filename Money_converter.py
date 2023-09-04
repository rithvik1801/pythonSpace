typeofmoney=str(input("Do you want to convert money from USD to INR or INR to USD."))
if typeofmoney == "USD to INR":
  amount=float(input("Type amount of money wanted to be calculated."))
  print(amount*81.50)
else:
  amount=float(input("Type amount of money wanted to be calculated."))
  print(amount/81.50)