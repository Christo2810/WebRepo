with open("stud.txt") as f:
	slist=f.readlines()
print(slist)
slist=[s.strip() for s in slist]
print("rain is comming")
print(slist)
