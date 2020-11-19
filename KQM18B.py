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
    

	s = input()
	n = len(s)
	dp = [[1 for i in range(n + 1)] for j in range(n + 1)]
	for i in range(n): dp[i + 1][i + 1] = 1
	i = n - 1
	maxi = 1
	while i >= 1:
	    for j in range(i + 1, n + 1):
	        if j - i == 1:
	            if s[i - 1] == s[j - 1]:
	                dp[i][j] = 2
	            else:
	                dp[i][j] = 1
	        else:
	            if s[i -1 ] == s[j - 1]:
	                dp[i][j] = 2 + dp[i + 1][j - 1]
	            else:
	                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
	        maxi = max(maxi, dp[i][j])
	    i -= 1
	print(n - maxi)


 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
