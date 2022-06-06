n = int(input())
if n == 0:
	print("yes")
elif n == 1:
	print("yes")
else:
	if n % 3 == 0 or n % 6 == 1:
		print("yes")
	else:
		print("no")