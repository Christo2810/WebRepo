import csv
import pandas
field=['name', 'age' , 'rollno']
sdict=[{'name':'christo','age':22,'rollno':28}, {'name':'sukuno','age':20,'rollno':24}]
with open("age.csv",'w') as dfile:
	writer=csv.DictWriter(dfile, fieldnames=field)
	writer.writeheader()
	writer.writerows(sdict)
data=pandas.read_csv("age.csv")
print (data)
