"""

    Author - AYUSHMAN CHAHAR #

"""
from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
#import numpy
from itertools import combinations
from itertools import permutations
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
sys.setrecursionlimit(10000000)

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
  
if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
 
        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
 
        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
 
def main():
	for _ in range(int(input())):
		tot, n = map(int, input().split())
		l1 = [int(i) for i in input().split()]
		rem = len(l1) % tot
		ans = True
		for i in range(0, len(l1) - rem, tot):
			l2 = l1[i: i + tot]
			#print(l2)
			if sorted(set(l2)) == [i + 1 for i in range(tot)]: ans = True
			else: ans = False; print("NO"); break
		if ans == True: print("YES")

     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 

######  ORRRRRRRR #########
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [int(i) for i in input().split()]
    count = [0] * n
    for i in arr:
        ans = True
        count[i - 1] += 1
        for j in range(n):
            if (j != (i - 1)  and  count[j] > count[i - 1]) or (count[i - 1] > (count[j] + 1)):
                ans = False
        if not ans:
            print("NO")
            break
        #print(count)
    if ans:
        print("YES")