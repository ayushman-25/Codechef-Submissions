for _ in range(int(input())):
	n = int(input())
	temp = n
	circles = 0
	while (temp >= 1):
		if int(temp ** (1 / 2)) == temp ** (1 / 2):
			circles += 1
			temp = n - temp
			n = temp
		else:
			temp -= 1 
	print(circles)