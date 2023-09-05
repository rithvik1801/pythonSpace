totalnums=int(input("How many numbers do you want to type?"))
y=0
greatest=0
z=0
while y < totalnums:
  z=int(input("Enter a number:"))
  if z>greatest:
    greatest=z
  y =+ 1 
print("Greatest Number:",greatest)