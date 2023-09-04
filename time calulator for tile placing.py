n=float(input("Enter the length of the square pavment in feet."))
l=float(input("Enter the length of the each tile in feet."))
w=float(input("Enter the width of the each tile in feet."))
o=float(input("Enter the length of the bench in feet."))
m=float(input("Enter the width of the bench in feet."))
narea=n*n
tilearea=l*w
bencharea=o*m
needtobetiledarea=narea-bencharea
numberoftiles=needtobetiledarea/tilearea
time=numberoftiles*0.2
print(time+" minutes")