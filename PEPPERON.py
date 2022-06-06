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
	a=input()
	for i in range(a):
	    l=[]
	    l1=[]
	    b=input()
	    for j in range(b):
	        c=raw_input()
	        l.append(c)
	    
	    for j in l:
	        c = 0
	        lol = 0
	        t = b/2
	        for k in j[:b/2]:
	            if k == "1":
	                c+=1
	            if j[t] == "1":
	                lol+=1
	            t+=1
	        l1.append(c-lol)
	    l3=[abs(sum(l1))]
	    l2=[]
	    l2.extend(l1)
	    for j in range(len(l1)):
	        l2[j]=-l2[j]
	        l3.append(abs(sum(l2)))
	        l2=[]
	        l2.extend(l1)
	    print min(l3)
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 