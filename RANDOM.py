from random import randint
n = int(input())
for _ in range(n):
	l1 = []
	start = -23452132
	end = 234341232
	size = randint(1, 30)
	print(size)
	for i in range(size):
		l1.append(randint(start, end))
	print(*l1)