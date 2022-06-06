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

def longest(a, n, k): 
    freq = [0] * n
    start = 0
    end = 0
    now = 0
    l = 0
    for i in range(n): 
        freq[a[i]] += 1
        if (freq[a[i]] == 1): 
            now += 1
        while (now > k) : 
            freq[a[l]] -= 1
            if (freq[a[l]] == 0): 
                now -= 1
            l += 1
        if (i - l + 1 >= end - start + 1): 
            end = i 
            start = l 
    return end - start + 1 

 
def main():
    for _ in range(int(input())):
	    n, k=map(int, input().split(" "))
	    lst=list(map(int, input().split(" ")))
	    maxi = 0
	    if(k == 2):
	        ctr = 0
	        while(True):
	            ele = lst[ctr]
	            count = 1
	            while(ctr != len(lst)-1):
	                ctr += 1
	                if(lst[ctr] != ele):
	                    break
	                else:
	                    count += 1
	                
	            if(count > maxi):
	                maxi = count
	            if(ctr >= len(lst)-1):
	                break
	        print(maxi)
	    else:
	        print(longest(lst, n, k - 1))
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
