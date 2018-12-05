x_max = 1000
y_max = 1000
width = 2 * x_max + 1

def map(x,y):
	x += x_max
	y += y_max
	return (y * width + x)

def unmap(i):
	x = i % width
	x -= x_max
	y = (i - x) / width
	y -= y_max
	return x, y

def test():
	import random as rand
	for i in range (0,100000):
		x = rand.randint(-x_max, x_max)
		y = rand.randint(-y_max, y_max)
		i_c = map(x,y)
		x_c, y_c = unmap(i_c)
		if (x !=  x_c or y != y_c):
			print ("Failed!")
			print ([x, y])
			print ([x_c, y_c])
			print (i_c)
			exit(1)
	print("All passed!")

test()
