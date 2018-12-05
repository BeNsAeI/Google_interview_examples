for i in range (0,100):
	myString = ""
	if i % 3 == 0:
		myString += "Fizz"
	if i % 5 == 0:
		 myString += "Buzz"
	if myString == "":
		myString = str(i)
	print myString
