def is_member(list_num,element):
	length = len(list_num)
	for i in list_num:
		if element == i:
			print('number is present in the list')
			return
	print('number is not present in list')

number =  input('Enter number of elements: ')
print('Enter numbers:')
list_num = []
for i in range(0,number):
	ele = input()
	list_num.append(ele)
element = input('Enter number to be searched ')
is_member(list_num,element)