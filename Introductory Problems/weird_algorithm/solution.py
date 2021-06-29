x = int(input())
while x != 1:
	print(x, end = " ")
	if x % 2 == 0:
		x //= 2
	else:
		x = 3 * x + 1
print(x)