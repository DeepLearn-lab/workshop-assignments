def vowelornot(char):
	if char in ('a','e','i','o','u','A','E','I','O','U'):
		return True
	else:
		return False

char = raw_input('Enter a character')
print(vowelornot(char))