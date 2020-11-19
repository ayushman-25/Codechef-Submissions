'''from sys import stdin, stdout
t, s = map(int, stdin.readline().split())
for _ in range(t):
	n = int(stdin.readline())
	chef = sorted([int(i) for i in stdin.readline().split()])
	friendd = sorted([int(i) for i in stdin.readline().split()])
	lenn = len
	if(n == 1):
		if(friendd[0] <= chef[0]):
			stdout.write("NO" + "\n")
		else:
			stdout.write("YES" + "\n")
	else:
		table = [chef[0], friendd[0]]
		i = -1
		while(1):
			if(lenn(chef) == 0 and lenn(friendd) == 0):
				stdout.write("YES" + "\n")
				break
			else:
				i += 1
				if chef[i] in table:
					val = chef[i]
					table.append(val)
					chef.remove(val)
					#ans = True
					if friendd[i] > val:
						table.append(friendd[i])
						friendd.remove(friendd[i])
						i =- 1
					else:
						stdout.write("NO" + "\n")
						break
					#for j in range(0, lenn(friendd)):
					#	if(friendd[j] > val):
					#		ans = True
					#		table.append(friendd[j])
					#		friendd.remove(friendd[j])
					#		i = -1
					#		break
					#	else:
					#		ans = False
					#if(ans == False):
					#	stdout.write("NO" + "\n")
					#	break
				else:
					stdout.write("NO" + "\n")
					break
'''

from sys import stdin, stdout
t, s = map(int, stdin.readline().split())
for _ in range(t):
	n = int(stdin.readline())
	chef = sorted([int(i) for i in stdin.readline().split()])
	friendd = sorted([int(i) for i in stdin.readline().split()])
	lenn = len
	if(n == 1):
		if(friendd[0] <= chef[0]):
			stdout.write("NO" + "\n")
		else:
			stdout.write("YES" + "\n")
	elif min(chef) >= max(friendd):
		stdout.write("NO" + "\n")
	
	else:
		table = [chef[0], friendd[0]]
		for i in range(len(chef)):
			if chef[i] in table:
				table.append(chef[i])
				if(friendd[i] > chef[i]):
					table.append(friendd[i])
				else:
					stdout.write("NO" + "\n")
					break
			else:
				stdout.write("NO" + "\n")
				break
			if i == len(chef) - 1:
				stdout.write("YES" + "\n")
				break