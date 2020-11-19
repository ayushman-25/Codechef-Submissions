n = int(input())
temp = n
print(n)
# arr = [i for i in range(1, n + 1)]
x = input()
asked = 1
eve, odd = 0, 0
if x == 'E': exit(0)
print(n)
#the following will contain some extra queries asked which we dont need to use.
while(True):
	x = input()
	if(x == 'G'):
		#spoken false
		asked += 1
		break
	else:
		asked += 1
		print(n)
print("first while ended")
#now when she speaks false, the above loop ends abruptly at asked th question.
#therefore she should have told true at asked - 1 th question
if (asked - 1) % 2  == 0:
	eve = 1
else:
	odd = 1
temp = 0
# if eve:
# 	#print("went1")
# 	l = 0
# 	r = n
# 	exception = False
# 	while(True):
# 		if r > l:
# 			mid = (l + (r - 1)) // 2
# 		elif r == l:
# 			mid = (l + r) // 2
# 		else:
# 			mid = (r + (l - 1)) // 2
# 		if exception: print(arr[l])
# 		else: print(arr[mid]) 
# 		s = input()
# 		asked += 1
# 		if s == 'E':
# 			exit(0)
# 		if l == r:
# 			exception = True
# 			continue
# 		if asked % 2 == 0:
# 			if s == 'L':
# 				l = mid + 1
# 				#print("l", l)
# 				#print("r", r)
# 			elif s == 'G':
# 				r = mid - 1
# 				#print("l", l)
# 				#print("r", r)
# if odd:
# 	#print("went2")
# 	l = 0
# 	r = n
# 	exception = False
# 	while(True):
# 		if r > l:
# 			mid = (l + (r - 1)) // 2
# 		elif r == l:
# 			mid = (l + r) // 2
# 		else:
# 			mid = (r + (l - 1)) // 2
# 		if exception: print(arr[l])
# 		else: print(arr[mid])
# 		#print("POSI", mid + 1)
# 		s = input()
# 		asked += 1
# 		if s == 'E':
# 			exit(0)
# 		if l == r:
# 			exception = True
# 			continue
# 		if asked % 2 != 0:
# 			if s == 'L':
# 				r = mid - 1
# 				#print("l", l)
# 				#print("r", r)
# 			elif s == 'G':
# 				l = mid + 1
# 				#print("l", l)
# 				#print("r", r)

if eve:
	l = 1
	r = n
	while(True):
		mid = (l + r + 1) // 2
		print(mid)
		print("L", l)
		print("R", r)
		print(asked)
		s = input()
		asked += 1
		if s == 'E':
			exit(0)
		if asked % 2 == 0:
			if s == 'L':
				r = mid - 1
			elif s == 'G':
				l = mid

if odd:
	l = 1 
	r = n
	while(True):
		mid = (l + r + 1) // 2
		print(mid)
		print("L", l)
		print("R", r)
		print(asked)
		s = input()
		asked += 1
		if s == 'E':
			exit(0)
		if asked % 2 != 0:
			if s == 'L':
				r = mid - 1
			elif s == 'G':
				l = mid