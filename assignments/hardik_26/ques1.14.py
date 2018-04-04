def common(list1,list2):
	length1 = len(list1)
	length2 = len(list2)
	for i in range(0,length1):
		for j in range(0,length2):
			if list1[i] == list2[j]:
				return True
	return False

number1 = input('Enter number of elements: ')
list1 = []
print('Enter elments: ')
for i in range(0,number1):
	ele = input()
	list1.append(ele)
number2 = input('Enter number of elements: ')
list2 = []
print('Enter elements: ')
for i in range(0,number2):
	ele = input()
	list2.append(ele)
print(common(list1,list2))