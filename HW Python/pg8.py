def check_word_presence():
	text=input("enter a text:")
	word=input("enter a word to check it presence")
	if word in text:
		print(f"{word}' is present in the text")
	else:
		print(f"{word}' is not present in the text")
check_word_presence()
