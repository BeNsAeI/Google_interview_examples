def cleaner(my_str):
	new_str = ""
	for i in my_str:
		if i not in new_str:
			new_str += i
	return new_str

def test():
	from numpy import random
	import string
	abs = string.lowercase+string.uppercase+string.digits+"!@#$%^&*()_+{}[]|\\/\'\"`~,.?"
	abs_list = []
	for i in abs:
		abs_list.append(i)
	for i in range (0, 1000):
		some_str = random.choice(abs_list, 50)
		normal_str = ""
		for i in some_str:
			normal_str += str(i)
		new_str = cleaner(normal_str)
		print ("> " + normal_str + " -> " + new_str)

test()
