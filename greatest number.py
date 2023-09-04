totalnums=int(input("How many numbers do you want to type?"))
lst= []
y=0
while totalnums > y:
  x=int(input("Enter a number:"))
  y += 1
  lst.append(x)
  lst.sort()

print("Your numbers",lst)
max=lst[len(lst)-1]
print("Maximum number:", max )