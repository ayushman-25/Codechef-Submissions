from sys import stdin, stdout

for _ in range(int(stdin.readline())):
	n, b = map(int, stdin.readline().split())
	tablet = []
	for _ in range(n):
		w, h, p = map(int, stdin.readline().split())
		if p <= b:
			tablet.append(w * h)
	if tablet == []: stdout.write("no tablet\n")
	else: stdout.write(str(max(tablet)) + "\n") 