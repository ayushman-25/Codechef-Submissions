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
		n = int(input())
		s = input()
		chancesA = n
		chancesB = n
		goalsA = 0
		goalsB = 0
		ans = True
		for i in range(len(s)):
			if i % 2 != 0:
				if s[i] == '1':
					goalsA += 1
					chancesA -= 1
				else:
					chancesA -= 1
			else:
				if s[i] == '1':
					goalsB += 1
					chancesB -= 1
				else:
					chancesB -= 1
			if (chancesB + goalsB) < goalsA or (chancesA + goalsA) < goalsB:
				print(i + 1)
				ans = True
				break
			else:
				ans = False
		if ans == False:
			print(n * 2)     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
