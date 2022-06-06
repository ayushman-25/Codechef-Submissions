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
        n, m = map(int, input().split())
        arr = [int(i) for i in input().split()]
        robot_moves = []
        for _ in range(m):
            a, b = map(int, input().split())
            robot_moves.append([a, b])
        #solving for m = 0;
        N_arr = [int(i) for i in range(1, n + 1)]
        minutes = 0
        ans_perm = [0] * n                  
        for i in range(n):
            vase = i + 1
            #print(arr[i] - 1)
            ans_perm[arr[i] - 1] += vase
        #print("Req Perm: ", ans_perm)
        #need to do the swapped till the ans_perm is achieved
        if ans_perm == N_arr:
            print(0)
        else:
            i = 0
            minutes = 0
            #print(N_arr)
            while(1):
                #find the inddex where we need to swap it
                getidx = ans_perm.index(N_arr[i])
                prev = N_arr[:]
                #print("Before Swapping: ", prev)
                tbs1 = i + 1
                tbs2 = getidx + 1
                if [tbs1, tbs2] in robot_moves:
                    N_arr[i], N_arr[getidx] = N_arr[getidx], N_arr[i]
                #print("After swapping: ", N_arr)
                #print(prev, N_arr)
                else:
                    N_arr[i], N_arr[getidx] = N_arr[getidx], N_arr[i]
                    if prev != N_arr:
                        minutes += 1
                if N_arr[i] == ans_perm[i]:
                    i += 1
                else:
                    i = 0
                if N_arr == ans_perm:
                    break
            print(minutes)       
     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
