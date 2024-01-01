def fact(x):
  if x==1:
    return 1
  else:
    return x*fact(x-1)
def npr(n,r):
  return (fact(n)/fact(n-r))

n=int(input("Enter n: "))
r=int(input("Enter r: "))

print("Result : ", npr(n,r))
fact(x)
