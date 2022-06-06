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
 
def fmi(index, a, curr):
	ans = -1
	index = 0
	for i in range(index, len(a)):
		if(a[i] > curr):
			if ans == -1:
				ans = curr
				index = i
			else:
				ans = min(ans, a[i])
				index = i
	return index

def np(nums):
	found = False
	i = len(nums) - 2
	while(i >= 0):
		if(nums[i] < nums[i + 1]):
			found = True
			break
		i -= 1
	if not found:
		nums.sort()
	else:
		m = fmi(i + 1, nums, nums[i])
		nums[i], nums[m] = nums[m], nums[i]
		nums[i + 1: ] = nums[i + 1: ][:: -1]
	return nums


def main():
    
     n, k = map(int, input().split())
	for _ in range(k):
		arr = [int(i) for i in input().split()]
		print(*np(arr))

 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
