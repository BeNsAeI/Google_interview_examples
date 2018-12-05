import re
import string

def list_handler(list):
	new_list = list
	list_len = len(new_list)
	for i in range(0,list_len):
		try:
			test = int(new_list[i][0])
		except:
			try:
				new_new_list = []
				count = int(new_list[i-1][0])
				tmp = ""
				for j in range(0,count):
					tmp += new_list[i][0]
				for j in range(0,i-1):
					new_new_list.append(new_list[j])
				new_new_list.append([tmp,new_list[i][1]-1])
				for j in range(i+1,len(new_list)):
					new_new_list.append(new_list[j])
				new_list = new_new_list
				list_len = len(new_list)
				print new_list
				new_list = list_handler(new_list)
			except:
				pass
	return new_list


def decompress(my_str):
	list = []
	new_list = []
	level = 0
	list = re.split("\[|\]", my_str)
	new_str = ""
	for i in list:
		if i != "":
			new_list.append([i,level])
		try:
			test = int(i)
			level += 1
		except:
			level -= 1
		if level < 0:
			level = 0
	print new_list
	new_list = list_handler(new_list)
	print new_list
	for i in new_list:
		new_str += i[0]
	return new_str

def test():
	some_str = "2[2[abc]]4[ab]c"
	new_str = decompress(some_str)
	if new_str != "abcabcabcabcababababc":
		print("Failed: " + some_str + " -> " + new_str)
		exit(1)
	else:
		print("Passed: " + some_str + " -> " + new_str)
test()
