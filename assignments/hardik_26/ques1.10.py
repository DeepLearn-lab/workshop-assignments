def reverse(string):
	rev_string = ''
	length = len(string)
	while length > 0:
		rev_string += string[length-1]
		length -= 1
	return rev_string

string = raw_input('Enter a string: ')
print(reverse(string))