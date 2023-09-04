#Write a program that inputs 2 * n integers and checks if the sum of the first n numbers (left sum) is equal to the sum of the second n numbers (right sum). If the sums are equal, print "Yes" + sum, if not, print "No" + difference. Calculate the difference as a positive number (absolute value).
# for git checkout
totalnum=int(input("How many numbers do you want to add? (Type only an even number.)"))
lrun=1
rrun=1
leftsum=0
rightsum=0
if totalnum%2!=0:
  print("Number is not even. Please try again.")
else:
  while lrun<=totalnum/2:
    xl=int(input("Type a number."))
    leftsum=leftsum+xl
    lrun=lrun+1
  while rrun<=totalnum/2:
    xr=int(input("Type a number."))
    rightsum=rightsum+xr
    rrun=rrun+1
if rightsum==leftsum:
  print("Yes:",rightsum)
elif rightsum<leftsum:
  print("No:", leftsum-rightsum)
else:
  print("No:", rightsum-leftsum)