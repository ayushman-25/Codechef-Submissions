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
		n = int(input())
		l1 = [int(i) for i in input().split()]
		l2 = [int(i) for i in input().split()]
		ans1 = True
		ans2 = True
		for i in range(n):
			if l1[i] <= l2[i]:
				ans1 = True
			else: ans1 = False; break
		for i in range(n):
			if l1[i] <= l2[n - i - 1]:
				ans2 = True
			else: ans2 = False; break
		if ans1 == ans2 == True:
			print("both")
		elif ans1 == ans2 == False:
			print("none")
		elif ans1 == True and ans2 == False:
			print("front")
		elif ans1 == False and ans2 == True:
			print("back")      
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 