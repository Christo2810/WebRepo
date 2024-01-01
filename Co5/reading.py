f=open("hel.txt", "r")
str=f.read(20);
print("string read is", str)
f.close()
print("file", f.name, "is closed")
