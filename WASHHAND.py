"""

    Author - AYUSHMAN CHAHAR #

"""
from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
# import numpy
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
        pop = list(input())
        d = int(input())
        dl = list(map(int, input().split()))
        status = ["NI"] * n

        for i in dl:
            status[i - 1] = 'I'
            if pop[0] == '1' and status[1] == 'NI':
                pop[1] = '1'
            temp = []
            for i in range(1, n - 1):
                if pop[i] == '1':
                    temp.append(i)
            for i in temp:
                if pop[i] == '1':
                    if status[i] == 'NI':
                        pop[i - 1] = '1'
                    if status[i + 1] == 'NI':
                        pop[i + 1] = '1'
            if pop[-1] == '1' and status[-1] == 'NI':
                pop[-2] = '1'
        print(pop.count('1'))


if __name__ == '__main__':
    sync_with_stdio(False)
    main()
