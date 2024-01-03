n=input("enter the numbers:")
b=[int(i) for i in n.split()]
smallest=min(b)
print("smallet element",smallest)

largest=max(b)
print("largest element",largest)

remove=list(set(b))
print(" not dulicate", remove)

num=input("enter the Numbers:")
c=[int(i) for i in num.split()]

append= b+c
print("combine", append)
