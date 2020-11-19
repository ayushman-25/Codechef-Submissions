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
		n, c = map(int, input().split())
		s = input()
		#condsider count - 1 for count greater than 1
		cnt = 0
		res = (list(Counter(s).most_common(n)))
		pend = []
		for i in res:
			if i[1] == 1:
				break
			else:
				pend.append(i[1])
		for _ in range(c):
			iso = int(input())
			if res[0][1] == 1 and (iso >= 1):
				print(0)
				continue
			if iso == 0:
				print(n)
				continue
			else:
				if pend == []:
					print(0)
				else:
					pendd = [i - 1 for i in pend]
					left_iso = iso - 1
					#print(pendd)
					#print(left_iso)
					ans = 0
					for i in pendd:
						if i <= left_iso:
							pass
						else:
							ans += abs(i - left_iso)
					print(ans) 
					
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
