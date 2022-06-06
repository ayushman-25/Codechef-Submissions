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
    
	for __ in range(int(input())):
	    a1, a2, a3, c1, c2, c3= map(int, input().split())
	    cnt = 3
	    if((a1 > a2 and c1 > c2) or (a2 > a1 and c2 > c1) or (a2 == a1 and c2 == c1)):
	        cnt -= 1
	    if((a2 > a3 and c2 > c3) or (a3 > a2 and c3 > c2) or (a3 == a2 and c3 == c2)):
	        cnt -= 1
	    if((a1 > a3 and c1 > c3) or (a3 > a1 and c3 > c1) or (a3 == a1 and c3 == c1)):
	        cnt -= 1   
	    if cnt == 0 :
	        print("FAIR")
	    else:
	        print("NOT FAIR")     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
