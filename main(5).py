f= open("numbers.txt","w")
f.write("1,2,3,4,5,6,7,8,9,10")
f.close()
f= open("numbers.txt","r")
f1= f.readline()
print(f1)
e= open("even.txt",'a')
o= open("odd.txt",'a')
for i in f:
  if(i%2==0):
    e.write(i)
  else:
    o.write(i)