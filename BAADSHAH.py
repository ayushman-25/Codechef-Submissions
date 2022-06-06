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
 
def getsum(BITTree, i): 
    s = 0
    i = i+1
    while i > 0: 
        s += BITTree[i] 
        i -= i & (-i) 
    return s 
  
def updatebit(BITTree, n, i, v): 
    i += 1 
    while i <= n: 
        BITTree[i] += v 
        i += i & (-i) 

def construct(arr, n): 
    BITTree = [0]*(n+1) 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 
    return BITTree

def main():

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    BITTree = construct(arr, n)
    for _ in range(m):
        tl = list(map(int, input().split()))
        if tl[0] == 1:
            val = arr[tl[1] - 1]
            arr[tl[1] - 1] += (tl[2] - val); 
            updatebit(BITTree, n, tl[1] - 1, tl[2] - val)
        else:
            found, low, high = False, 0, n   
            while(low <= high):
                mid = low + (high - low) // 2
                val = getsum(BITTree, mid)
                if(val == tl[1]):
                    print("Found", mid + 1)
                    found = True
                    break
                elif(val < tl[1]):
                    low = mid + 1
                else:
                    high = mid - 1
            if not found:
                print("Not Found")

if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
