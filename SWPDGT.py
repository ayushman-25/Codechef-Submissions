
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
        a, b = map(int, input().split())
        sa = str(a)
        sb = str(b)
        if len(sa + sb) == 2:
            print(a + b)
        elif len(sa + sb) == 3:
            combined = [i for i in (sa + sb)]
            if len(sa) == 1 and len(sb) == 2:
                list1 = [int(int(combined[1]) + int(combined[0] + combined[2])) ,int(int(combined[2]) + int(combined[1] + combined[0])), a + b]
                print(max(list1))
            else:
                list1 = [int(int(combined[2] + combined[1]) + int(combined[0])), int(int(combined[0] + combined[2]) + int(combined[1])), a + b]
                print(max(list1))
        else:
            combined = [i for i in (sa + sb)]
            #print(combined)
            list1 = [int(int(combined[2] + combined[1]) + int(combined[0] + combined[3])), int(int(combined[0] + combined[3]) + int(combined[2] + combined[1])), int(int(combined[3] + combined[1]) + int(combined[2] + combined[0])), int(int(combined[0] + combined[2]) + int(combined[1] + combined[3])), a + b]
            print(max(list1))     

if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
