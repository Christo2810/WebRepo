def remove_duplicates():
	items=input("enter a list of items separated by space:").split()
	unique_items=list(set(items))
	print("list after removing duplicates:", unique_items)
remove_duplicates()
