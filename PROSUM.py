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
from math import factorial
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

def ncr(n, r):
	return factorial(n) // ((factorial(r)) * factorial(n - r))

def main():
	for _ in range(int(input())):
		n = int(input())
		l1 = [int(i) for i in input().split()]
		cnt0, cnt1, cnt2 = 0, 0, 0
		for i in l1:
			if i == 0: cnt0 += 1
			elif i == 1: cnt1 += 1
			elif i == 2: cnt2 += 1
		if cnt2 > 1:
			N = n - cnt0 - cnt1 - ncr(cnt2, 2)
			if N >= 2: print(ncr(N, 2))
			else: print(0)
		else:
			N = n - cnt0 - cnt1
			if N >= 2: print(ncr(N, 2))
			else: print(0)
     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
