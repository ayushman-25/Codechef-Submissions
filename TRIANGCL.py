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
 

def dist(x, y, xx, yy):
	dist = (pow((yy - y), 2) + pow((xx - x), 2))
	return int(dist)

def assign(s1, s2):
	ans = list(s2.split())
	ans.insert(1, " " + s1 + " ")
	return(str("".join(ans)))



def main():

	sub_id = int(input())
	for _ in range(int(input())):
		x1, y1, x2, y2, x3, y3 = map(int, input().split())
		dist1 = dist(x1, y1 , x2, y2)
		dist2 = dist(x2, y2, x3, y3)
		dist3 = dist(x1, y1, x3, y3)
		#dist1 = float(format(dist(x1, y1, x2, y2), '.6f'))
		#dist2 = float(format(dist(x2, y2, x3, y3), '.6f'))
		#dist3 = float(format(dist(x3, y2, x1, y1), '.6f'))
		#checks begin
		'''
		if abs(dist1 - dist2) < (10 ** (-6)):
			#print("YES1")
			dist1 = dist2
		elif abs(dist2 - dist3) < (10 ** (-6)):
			dist2 = dist3
			#print("YES2")
		elif abs(dist3 - dist1) < (10 ** (-6)):
			dist3 = dist1
			#print("YES3")
		'''
		#checks end
		typeot = ""

		if(dist1 == dist2):
			typeot = "Isosceles triangle"
		elif(dist2 == dist3):
			typeot = "Isosceles triangle"
		elif(dist3 == dist1):
			typeot = "Isosceles triangle"
		else:
			typeot = "Scalene triangle"
		if sub_id == 1:
			print(typeot)
		else:
			#print(dist1, dist2, dist3)
			#print(float(10 ** (-6)))
			#check the angle as well;
			if dist1 + dist2 == dist3:
				print(assign("right", typeot))
			elif dist2 + dist3 == dist1:
				print(assign("right", typeot))
			elif dist1 + dist3 == dist2:
				print(assign("right", typeot))
			else:
				maxd = max(max(dist1, dist2), dist3)
				if maxd == dist1:
					if(dist1 < (dist2 + dist3)):
						print(assign("acute", typeot))
					else:
						print(assign("obtuse", typeot))
				elif maxd == dist2:
					if(dist2 < (dist1 + dist3)):
						print(assign("acute", typeot))
					else:
						print(assign("obtuse", typeot))
				else:
					if(dist3 < (dist1 + dist2)):
						print(assign("acute", typeot))
					else:
						print(assign("obtuse", typeot))
	     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
