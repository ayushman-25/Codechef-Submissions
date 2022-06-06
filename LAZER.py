'''for _ in range(int(input())):
	n, q = map(int, input().split())
	arr1 = [int(i) for i in input().split()]
	max1 = max(arr1)
	min1 = min(arr1)
	ls = []
	for i in range(0, len(arr1) - 1):
		ls.append([arr1[i], arr1[i + 1]])
	for _ in range(q):
		x1, x2, y = map(int, input().split())
		if x1 > y:
			print(0)
		elif x2 < y:
			print(0)
		else:
			cnt = 0
			for i in ls:
				if y in sorted([i for i in range(min(i), max(i) + 1)]):
					cnt += 1
			print(cnt)
'''
import atexit, io, sys

buffer = io.BytesIO()
sys.stdout = buffer

@atexit.register
def write():
	sys.__stdout__.write(buffer.getvalue())

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
def orientation(p, q, r):  
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 
        return 1
    elif (val < 0): 
        return 2
    else: 
        return 0
def doIntersect(p1,q1,p2,q2):  
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1)  
    if ((o1 != o2) and (o3 != o4)): 
        return True
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True 
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True 
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True 
    return False

for _ in range(int(input())):
	n, q = map(int, input().split())
	arr1 = [int(i) for i in input().split()]
	ls = []
	for _ in range(q):
		x1, x2, y = map(int, input().split())
		cnt = 0
		p1 = Point(x1, y)
		q1 = Point(x2, y)
		for i in range(len(arr1) - 1):
			p2 = Point(i + 1 ,arr1[i])
			q2 = Point(i + 2 ,arr1[i + 1])
			if doIntersect(p1, q1, p2, q2):
				cnt += 1
			if (i + 2 == x1 and arr1[i + 1] == y) or (i + 1 == x2 and arr1[i] == y):
				cnt -= 1
		print(cnt)
	