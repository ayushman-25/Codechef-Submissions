from random import randint

for _ in range(int(input())):
	n, m, k = map(int, input().split())
	answers = [[] for _ in range(k)]
	for i in range(n):
		qqs = list(map(int, input().split()))
		for i in range(len(qqs)):
			answers[i].append(qqs[i])

	print(answers)