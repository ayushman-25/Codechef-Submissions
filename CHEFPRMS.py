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
 
def isPrime(n):
    if n == 1:
        return 0
    if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return 1
    return 0

def main():

    for _ in range(int(input())):
        ans = False
        N = int(input())
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                if(i + j == N):
                    #check both i and j are semi prime or not
                    ansi = False
                    ansj = False
                    for k in range(1, i + 1):
                        for l in range(k, i + 1):
                            if((k * l == i) and (k != l)):
                                if(isPrime(k) and isPrime(l)):
                                    ansi = True
                                    break
                        if ansi:
                            break
                    for k in range(1, j + 1):
                        for l in range(k, j + 1):
                            if((k * l == j) and (k != l)):
                                if(isPrime(k) and isPrime(l)):
                                    ansj = True
                                    break
                        if ansj:
                            break
                    if ansi and ansj:
                        ans = True
                        break
            if ans:
                print("YES")
                break
        if not ans:
            print("NO")
     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
    