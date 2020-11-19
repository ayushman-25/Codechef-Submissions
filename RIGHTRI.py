cnt = 0
for _ in range(int(input())):
	x1, y1, x2, y2, x3, y3 = map(int, input().split())
	dis1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
	dis2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2)
	dis3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2)
	if dis1 + dis2 == dis3 or dis2 + dis3 == dis1 or dis1 + dis3 == dis2:
		cnt += 1
print(cnt)