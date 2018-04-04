def translate(string):
	new_string = '';
	for char in string:
		if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
			if char in ('a','e','i','o','u','A','E','I','O','U'):
				new_string += char
			else:
				new_string += (char + 'o' + char)
		else:
			new_string += char
	return new_string

string = raw_input('Enter a string : ')
print(translate(string))