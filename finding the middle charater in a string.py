string123=input("Type anything.")
if len(string123) % 2 == 0:
  middle=int((len(string123)/2)-1)
else:
  middle=int((len(string123)/2)-0.5)
print(string123[middle])