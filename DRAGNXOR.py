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
		bits, a, b = map(int, input().split())
		bina, binb = list(bin(a)[2: ]), list(bin(b)[2: ])
		while(len(bina) < bits):
			bina.insert(0, '0')
		while(len(binb) < bits):
			binb.insert(0, '0')
		combined = str("".join(bina + binb))
		c0 = combined.count('0')
		c1 = combined.count('1')
		if c1 == bits:
			print(2 ** bits - 1)
		else:
			my_string = ""
			if c1 < bits:
				for i in range(c1):
					my_string += '1'
				for i in range(bits - c1):
					my_string += '0'
				print(int(my_string, 2))
			else:
				for i in range(c0):
					my_string += '1'
				for i in range(bits - c0):
					my_string += '0'
				print(int(my_string, 2))     
	 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
