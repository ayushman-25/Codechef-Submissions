#for subtask 1
'''t, s = map(int, input().split())
for i in range(t):
	n = int(input())
	l1 = sorted([int(i) for i in input().split()])
	l2 = sorted([int(i) for i in input().split()])
	if l1[0] > l2[-1]:
		print("NO")
	elif list(set(l1)) == list(set(l2)):
		print("NO")
	else:
		
		iter1 = 0
		while 1:
			if l1[iter1] not in table:
				print("NO")
				break
			else:
				if len(l2) == 1 and l1[-1] < l2[0]:
					print("YES")
					break
				else:
					ans = True
					for j in range(len(l2)):
						if l2[j] > l1[iter1]:
							table.append(l2[j])
							l2.remove(l2[j])
							iter1 = 0
							ans = True
							break
						else:
							ans = False
							continue
					if ans == False:
						table.append(l1[iter1])
						iter1 += 1
			
		iter1 = 0
		table = [l1[0], l2[0]]
		l1.remove(l1[0])
		l2.remove(l2[0])
		while 1:
			if len(l1) == 0 and len(l2) == 0:
				print("YES")
				#print("DONE")
			if l1[iter1] not in table and len(l1) == 1:
				print("YES")
				#print("DONE1")
				break
			elif l1[iter1] not in table and len(l1) > 1:
				print("NO")
				break
			elif len(l2) == 1 and len(l1) == 1 and l1[0] < l2[0]:
				print("YES")
				#print("DONE2")
				break
			elif len(l2) == 1 and len(l1) == 1 and l1[0] > l2[0]:
				print("NO")
			else:
				ans = True
				for j in range(len(l2)):
					if l2[j] > l1[iter1]:
						table.append(l2[j])
						table.append(l1[iter1])
						l1.remove(l1[iter1])
						l2.remove(l2[j])
						ans = True
						iter1 = 0
						break
					else:
						ans = False
				if ans == False:
					iter1 += 1
'''

from collections import Counter
t, s = map(int, input().split())
for _ in range(t):
	n = int(input())
	l1 = ([int(i) for i in input().split()])
	l2 = ([int(i) for i in input().split()])
	min1 = min(l1); min2 = min(l2)
	a = Counter(l1 + l2)
	if min2 <= min1:
		print("NO")
	elif a.most_common(1)[0][1] == 1:
		print("NO")
	else:
		table = [min1, min2]
		i = 0
		while True:
			if len(l1) == 0 or len(l2) == 0:
				print("YES")
				break
			else:
				bool1 = True
				if l1[i] in table:
					ans = True
					for j in range(len(l2)):
						if l2[j] in table and l2[j] > l1[i]:
							ans = True
							table.append(l2[j])
							l2.remove(l2[j])
							i = 0
							break
						else:
							ans = False
							continue
					if ans == False:
						print("NO")
						break
				else:
					bool1 = False
					print("NO")
					break
				i += 1




































