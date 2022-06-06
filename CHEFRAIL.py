from itertools import combinations
for _ in range(int(input())):
	    n, m = map(int, input().split())
	    ln = [int(i) for i in input().split()]
	    lm = [int(i) for i in input().split()]
	    cnt = 0
	    lnc = list(combinations(ln, 2))
	    print(lnc)
	    lmc = list(combinations(lm, 2))
	    print(lmc)
	    for i in lmc:
		    for j in ln:
			    dis1 = (i[1] ** 2 + j ** 2)
			    dis2 = (i[0] ** 2 + j ** 2) 
			    dis3 = abs(i[0] - i[1]) ** 2 #same axis distance ** 2
			    if dis1 + dis2 == dis3 or dis1 + dis3 == dis2 or dis2 + dis3 == dis1:
				    cnt += 1
	    for i in lnc:
		    for j in lm:
			    dis1 = (i[1] ** 2 + j ** 2)
			    dis2 = (i[0] ** 2 + j ** 2) 
			    dis3 = abs(i[0] - i[1]) ** 2 #same axis distance ** 2
			    if dis1 + dis2 == dis3 or dis1 + dis3 == dis2 or dis2 + dis3 == dis1:
			    	cnt += 1
	    print(cnt)