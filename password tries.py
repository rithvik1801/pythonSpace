password="Code"
tries=0
input1=input("Enter the password")
if input1==password:
  print("Sucessfully loged-in")
  
else:
  while input1!=password:
    print("Wrong password. Try again.")
    tries=tries+1
    if tries==3:
      print("Account Locked.")
      break
    input1=input("Enter the password")
    if input1==password:
      print("Sucessfully loged-in")
      break