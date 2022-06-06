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
        n, k = map(int, input().split())
        arr = [int(i) for i in input().split()]
        if k == 1 or n == 1:
            print("yes")
        else:
            res = [0] * n
            x = []
            for i in range(k):
                temp = [] #contains val, index
                start = i
                for j in range(i, n, k):
                    temp2 = [arr[j]]
                    temp.append(temp2)
                temp.sort()
                x.append(temp)
            for i in range(len(x)):
                start = i
                for j in x[i]:
                    res[i] += j[0]
                    i += k

            if res == sorted(arr):
                print("yes")
            else:
                print("no")
                #print(res)
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 

