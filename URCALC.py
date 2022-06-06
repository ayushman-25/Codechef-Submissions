for  _ in range(int(input())):
	a, b, c = int(input()), int(input()), input()
	if c == '+':
		print(a + b)
	elif c == '-':
		print(a - b)
	elif c == '*':
		print(a * b)
	else:
		print(a / b)