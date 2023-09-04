num=int(input("Type the number which you want to calculate it's bonus."))
if num>1000:
  if num%2==0:
    bonus=(num*0.10)+1
    print(bonus)
  elif num%2!=0 and num%5==0 and num%10!=0:
    bonus=(num*0.10)+2
    print(bonus)
  else:
    bonus=(num*0.10)
    print(bonus)
elif num>100:
  if num%2==0:
    bonus=(num*0.20)+1
    print(bonus)
  elif num%2!=0 and num%5==0 and num%10!=0:
    bonus=(num*0.20)+2
    print(bonus)
  else:
    bonus=(num*0.20)
    print(bonus)
elif num<=100:
  if num%2==0:
    bonus=6
    print(bonus)
  elif num%2!=0 and num%5==0 and num%10!=0:
    bonus=7
    print(bonus)
  else:
    bonus=5
    print(bonus)