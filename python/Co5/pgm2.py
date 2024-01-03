s=open("stud.txt","r")
o=open("odd.txt","w")
e=open("even.txt","w")
contents=s.readlines()
print("The contents of file are:")
print(contents)
for i in range(len(contents)):
  if(i%2==0):
     e.write(contents[i])
  else:
     o.write(contents[i])
s.close
