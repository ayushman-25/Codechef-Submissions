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

def product(arr):
	prod =1 
	for i in arr:
		prod *= i
	return prod

def main():
    
	'''for _ in range(int(input())):
	n = int(input())
	arr = [int(i) for i in input().split()]

	#first checking for odd values
	cntodd = 0
	oddarray = []
	tempcnt = 0
	for i in range(n):
		if arr[i] & 1:
			tempcnt += 1
		else:
			oddarray.append(tempcnt)
			tempcnt = 0
			oddarray.append(tempcnt)
		if i == n - 1:
			oddarray.append(tempcnt)
	for i in oddarray:
		if  >= 1:
			cntodd += (i * (i + 1) // 2)
	print(cntodd)

	#now checking for module 4 thingy
	cnt4 = 0
	for i in range(n):
		if arr[i] >= 4 and arr[i] % 4 == 0:
			cnt4 += (n - i)
		else:
			prod = 1
			for j in range(i, n):
				prod *= arr[j]
				if prod >= 4 and (prod % 4 == 0):
					cnt4 += (n - j)
					break
	print(cnt4)

	'''
	for _ in range(int(input())):
		n = int(input())
		arr = [int(i) for i in input().split()]
		indexes = []
		elements = []
		for i in range(len(arr)):
			if arr[i] % 2 == 0:
				elements.append(arr[i])
				indexes.append(i)
		#indexes.append(n)
		#elements.append(-1)
		TOTAL = n * (n + 1) // 2
		cnt = 0
		'''
		if len(indexes) == 2 or len(elements) == 2:
			print("MY WAY1", TOTAL)
			print(indexes)
		elif len(indexes) == 3 or len(elements) == 3:
			if elements[1] != 0 and ((elements[1] // 2) & 1):
				if indexes[1] == 0:
					cnt += n
				elif indexes[1] == n - 1:
					cnt += n
				else:
					cnt += (n + 1)
			print("MY WAY2", TOTAL - cnt)
			print(indexes)
		else:
			for i in range(1, len(indexes) - 1):
				if elements[i] != 0 and indexes[i] != 0 and indexes[i] != n - 1 and ((elements[i] // 2) & 1):
					cnt += (indexes[i] - indexes[i - 1] + indexes[i + 1] - indexes[i])
					cnt += 1
				elif elements[i] != 0 and indexes[i] == 0 and ((elements[i] // 2) & 1):
					cnt += (indexes[i] - indexes[i - 1] + indexes[i + 1] - indexes[i])
					cnt += 1
				elif elements[i] != 0 and indexes[i] == n - 1 and ((elements[i] // 2) & 1):
					#cnt += (indexes[i] - indexes[i - 1])
					cnt += (indexes[i] - indexes[i - 1] + n - indexes[i] - 1)
					#cnt += 1
			print("MY WAY3", TOTAL - cnt)
			print(indexes)
		if len(indexes) == 1:
			if elements[0] != 0 and ((elements[0] // 2) & 1):
				if indexes[0] == 0 or indexes[0] == n - 1:
					cnt += n
				else:
					cnt += (indexes[0] - 0 + n - 1 - indexes[0] + 2)
			print(indexes)
			print("cnt", cnt)
			print("MY WAY1", TOTAL - cnt)
		elif len(indexes) >= 2:
			for i in range(len(indexes)):
				if elements[i] != 0 and ((elements[i] // 2) & 1):
					if i == 0:
						if indexes[i] == 0:
							cnt += (indexes[i] - 0 + indexes[i + 1] - indexes[i])
						else:
							cnt += (indexes[i] - 0 + indexes[i + 1] - indexes[i] + 1)
					elif i == len(indexes) - 1:
						if indexes[i] == n - 1:
							cnt += (n - indexes[i] + indexes[i] - indexes[i - 1] - 1)
						else: 
							cnt += (n - indexes[i] + indexes[i] - indexes[i - 1])
					else:
						cnt += (indexes[i] - indexes[i - 1] + indexes[i + 1] - indexes[i])
			print(indexes)
			print("cnt", cnt)
			print("MY WAY2", TOTAL - cnt)
		else:
			print(TOTAL)
		'''
		if len(indexes) == 0:
			print("MY WAY", TOTAL)
		elif len(indexes) == 1:
			if elements[0] != 0 and ((elements[0] // 2) & 1):
				if indexes[0] == 0 or indexes[0] == n - 1:
					cnt += n
				else:
					cnt += ((indexes[0] + 1) * (n - indexes[0]))
			print("MY WAY", TOTAL - cnt)
		else:
			for i in range(len(indexes)):
				if elements[i] != 0 and ((elements[i] // 2) & 1):
					#print(elements[i])
					#print(cnt)
					if i == 0:
						lh  = indexes[i] - 0
						rh = indexes[i + 1] - indexes[i]
						total = lh + rh		
						cnt += ((lh + 1) * (total - lh))
					elif i == len(indexes) - 1:
						lh = indexes[i] - indexes[i - 1]
						rh = n - 1 - indexes[i]
						total = lh + rh
						cnt += ((lh) * (total - lh + 1))
					#elif i == len(indexes) // 2:
					#	print("GONE")
					#	lh = indexes[i] - indexes[i - 1] - 1
					#	rh = indexes[i + 1] - indexes[i] - 1
					#	total = lh + rh + 1
					#	cnt += ((lh + 1) * (lh + 1))
					#	print(((lh + 1) * (lh + 1)))
					else:
						lh = indexes[i] - indexes[i - 1] - 1
						rh = indexes[i + 1] - indexes[i] - 1
						total = lh + rh + 1
						if ((total & 1) and (total // 2 == (lh))):
							cnt += ((lh + 1) * (lh + 1))
						else:
							cnt += ((lh + 1) * (total - lh))
			print(indexes)
			print("MY WAY", TOTAL - cnt)
		#brute force
		'''
		cntt = 0
		for i in range(n):
			prod = 1
			for j in range(i, n):
				prod *= arr[j]
				#print(prod)
				if (prod % 4 == 0 or (prod & 1) or prod == 0):
					#print("RIGHT", prod)
					cntt += 1
				#else:
					#print("WRONG", prod)
		print("BRUTE FORCE", cntt)  
		'''
		
		#cntttt = 0
		#for i in range(n):
		#	for j in range(i + 1, n + 1):
		#		if product(arr[i: j]) % 4 != 2:
		#			cntttt += 1
		#print("BRUTE FORCE", cntttt)     
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
 
