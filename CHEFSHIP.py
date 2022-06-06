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
        arr = input()
        n = len(arr)
        half = n // 2
        ways = 0
        #splitting into n - 1 ways
        halfhalf = half // 2
        start = 1
        for i in range(halfhalf):
            first, second = start, half - start
            #now check for first first second second and second second first first
            #print(first, second)
            #print(arr[0: first], arr[first: first + first])
            #print(arr[first + first: first + first + second], arr[first + first + second: first + first + second + second])
            prev_ways = ways
            if arr[0: first] == arr[first: first + first] and arr[first + first: first + first + second] == arr[first + first + second: first + first + second + second]:
                ways += 1
            if arr[0: second] == arr[second: second + second] and arr[second + second: first + second + second] == arr[first + second + second: first + first + second + second]:
                ways += 1
            after_ways = ways
            if first == second and (after_ways - prev_ways == 2):
                ways -= 1
            start += 1
        print(ways)  
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 

