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

    for i in range(int(input())):
        n, m, x, y=map(int,input().split())
        if (x == 0 and m % 2 == 0) or (y == 0 and n % 2 == 0) or (x == 0 and y == 0):
            print("YES")
        else:
            if (n * x + m * y) % 2 != 0:
                print("NO")
            elif n == 0 or m == 0:
                if n % 2 != 0 or m % 2 != 0:
                    print("NO")
                else:
                    print("YES")
            
            else:
                f = 0
                su = (n * x + m * y) // 2
                if n < m:
                    for i in range(n):
                        if (su - i * x) / y == (su - i * x) // y and ((su - i * x) // y) <= m:
                            print("YES")
                            f = 1
                            break
                    if f == 0:
                        print("NO")
                else:
                    for i in range(m):
                        if (su - i * y) / x == (su - i * y) // x and ((su - i * y) // x) <= n:
                            print("YES")
                            f = 1
                            break
                    if f == 0:
                        print("NO")
     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
