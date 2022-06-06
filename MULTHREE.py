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
	    k, d0, d1=map(int, input().split())
	    d2 = (d0 + d1) % 10
	    d3 = (d2 * 2) % 10
	    d4 = (d3 * 2) % 10
	    d5 = (d4 * 2) % 10
	    d6=(d5 * 2) % 10
	    l=[d3, d4, d5, d6]
	    if k == 2:
	        if(d0 + d1) % 3 == 0:
	            print("YES")
	        else:
	            print("NO")
	    elif k == 3:
	        if (d0 + d1 + d2) % 3 == 0:
	            print("YES")
	        else:
	            print("NO")
	    else:
	        sm = (d0 + d1 + d2) + (d3 + d4 + d5 + d6) * ((k - 3) // 4)
	        sm += sum(l[: (k - 3) % 4])
	        if sm % 3 == 0:
	            print("YES")
	        else:
	            print("NO")
            
    	     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
