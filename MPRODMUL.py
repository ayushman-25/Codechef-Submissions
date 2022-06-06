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
 
def product(n):
	s = str(n)
	prod = 1
	for i in s:
		prod *= int(i)
	return prod

def main():
    
	for _ in range(int(input())):
		a, b, k = map(int, input().split())
		ans = []
		productt = []
		for i in range(a, b + 1):
			if i % k == 0 and '0' not in str(i):
				string = str(i)
				anss = False
				for j in range(0, len(string) - 1):
					flag = 0
					for x in range(j + 1, len(string)):
						if int(string[j]) % int(string[x]) == 0:
							flag = 1
							break
						else:
							flag = 0
					if flag == 1:
						anss = True
					else:
						anss = False
						break
				if anss == True:
					productt.append(product(i))
					ans.append(i)
		if ans != []:
			maxns = max(productt)
			min1 = 99999999999
			for i in range(len(ans)):
				if productt[i] == maxns:
					if ans[i] < min1:
						min1 = ans[i]
			print(product(min1), min1)
		else:
			print(-1) 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
