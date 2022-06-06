def find_dist(x1, y1, x2, y2):
	return (int((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2))

for _ in range(int(input())):
	dist = int(input())
	x1, y1 = map(int, input().split())
	x2, y2 = map(int, input().split())
	x3, y3 = map(int, input().split())
	cnt = 0
	if find_dist(x1, y1, x2, y2) <= dist:
		cnt += 1
	if find_dist(x2, y2, x3, y3) <= dist:
		cnt += 1
	if find_dist(x1, y1, x3, y3) <= dist:
		cnt += 1
	if cnt >= 2:
		print("yes")
	else: print("no")