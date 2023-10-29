
x=input("Type anything.")
y=""
ystatz=False
uqstatz=False
ustatz=False
ac= x.find('a')
ec= x.find('e')
ic= x.find('i')
oc= x.find('o')
uc= x.find('u')
yc=0


if x.startswith("y"):
  ystatz=True

if not ystatz:
  z=x.find("y")

if uc>ac or uc>ec or uc>ic or uc>oc or uc>uc or uc>yc:
  ustatz=True



if ustatz and  x.index("q")==uc-1:
  y=x[uc+1:len(x)]+x[0:uc+1]+"ay"
  print(y)


if x[0]=="a"or x[0]=="e"or x[0]=="i"or x[0]=="o"or x[0]=="u":
  print(x+"way")
else:
  for i in range(0,len(x)):
    if not ystatz and x[i]=="a"or x[i]=="e"or x[i]=="i"or x[i]=="o"or x[i]=="u"or x[i]=="y":
      y=x[i:len(x)]+x[0:i]+"ay"
      break
    if x[i]=="a"or x[i]=="e"or x[i]=="i"or x[i]=="o"or x[i]=="u":
      y=x[i:len(x)]+x[0:i]+"ay"
      break
print(y)
