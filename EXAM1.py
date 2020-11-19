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
		correct = input()
		chef = input()
		ans = []
		marks = 0
		if n >= 3:
			if chef[0] == correct[0]:
				ans.append("Correct")
			elif chef[0] != correct[0] and chef[0] != 'N':
				ans.append("Wrong Answer")
			elif chef[0] != correct[0] and chef[0] == 'N':
				ans.append("Not Attempted")

			for i in range(1, n - 1):
				if ans[-1] == "Wrong Answer":
					ans.append("Skipped")
				else:
					if chef[i] == correct[i]:
						ans.append("Correct")
					elif chef[i] != correct[i] and chef[i] != 'N':
						ans.append("Wrong Answer")
					elif chef[i] != correct[i] and chef[i] == 'N':
						ans.append("Not Attempted")
			if ans[-1] == "Wrong Answer":
					ans.append("Skipped")
			else:
			    if chef[-1] == correct[-1]:
			        ans.append("Correct")
			    elif chef[-1] != correct[-1] and chef[-1] != 'N':
			        ans.append("Wrong Answer")
			    elif chef[-1] != correct[-1] and chef[-1] == 'N':
			        ans.append("Not Attempted")
		else:
			if n == 1:
				if chef[0] == correct[0]:
					ans.append("Correct")
				else:
					ans.append("Wrong Answer")
			elif n == 2:
				if chef[0] == correct[0] and chef[1] == correct[1]:
					ans.append("Correct")
					ans.append("Correct")
				elif chef[0] != correct[0] and chef[0] != 'N':
					ans.append("Wrong Answer")
					ans.append("Skipped")
				elif chef[0] != correct[0] and chef[0] == 'N':
					ans.append("Not Attempted")
					if chef[1] == correct[1]:
						ans.append("Correct")
					else:
						ans.append("Wrong Answer")
		#print(*ans)
		for i in ans:
			if i == "Correct": marks += 1
		print(marks)

if __name__ == "__main__":
	sync_with_stdio(False)
	main()