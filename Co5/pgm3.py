import csv
with open('age.csv','r') as file:
	data=csv.reader(file)
	for i in data:
		print(i)
