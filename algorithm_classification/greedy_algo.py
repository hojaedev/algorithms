

'''
HackerRank
Greedy Algorithm
Reverse Shuffle Merge
'''
from collections import Counter, defaultdict
from bisect import bisect

def solve(s):
    word = Counter(s)
    for k, v in word.items():
        word[k] = v // 2
    revleft = word.copy()
    skipped, avail = Counter(), Counter()
    locs = defaultdict(list)
    for i, c in enumerate(s):
        locs[c].append(i)
    ans = []
    live = len(s) - 1
    dead = len(s)
    while revleft:
        leftc = s[live]
        avail[leftc] += 1
        while avail[leftc] + skipped[leftc] > word[leftc]:
            cnew = min(c for c in avail.keys() if avail[c] > 0 and revleft[c] > 0)
            ans.append(cnew)
            avail[cnew] -= 1
            revleft[cnew] -= 1
            if revleft[cnew] == 0:
                del revleft[cnew]
            i = bisect(locs[cnew], dead - 1) - 1
            #            print(i)
            i = locs[cnew][i]
            assert s[i] == cnew
            for c in s[i + 1: dead]:
                avail[c] -= 1
                skipped[c] += 1

            dead = i
            assert live <= i
        live -= 1
    return ''.join(ans)

'''
1139
'''
def solve(arr):
    arr.sort()
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] * (len(arr)-i)
    return sum

print(solve([3,1,4,3,2]))


'''
11047
'''

def solve(money, coin):
    count = 0
    for m in reversed(coin):
        count += money // m
        money = money % m

    return count

n, money = map(int, input().split(" "))
coin = []
for _ in range(n):
    coin.append(int(input()))

print(solve(money, coin))


'''
1931
'''
import sys

def solve(timeslots):

    timeslots.sort(key=lambda x: x[1])

    count = 0

    if len(timeslots) == 0:
        return 0

    prev = None

    for i in range(len(timeslots)):

        if timeslots[i]:

            if prev:

                if timeslots[i][0] >= prev[1]:

                    prev = timeslots[i]

                    count += 1

                else:

                    continue

            else:

                prev = timeslots[i]

                count += 1

    return count

n = int(sys.stdin.readline().rstrip())
inp = []
for _ in range(n):
    inp.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
print(solve(inp))

'''
Greedy Algo - Luck Balance
'''
import math
import os
import random
import re
import sys


def luckBalance(k, contests):
    contests.sort(key=lambda x: x[0], reverse=True)
    count = 0
    lose = 0
    s = 0
    for i in range(len(contests)):
        if contests[i][1] == 1:
            if count < k:
                s += contests[i][0]

            else:
                lose += contests[i][0]
            count += 1
        else:
            s += contests[i][0]
    return s - lose

nk = input().split()

n = int(nk[0])

k = int(nk[1])

contests = []

for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))

result = luckBalance(k, contests)

print(result)


'''
HackerRank
Greedy Algorithm
Greedy Florist
'''
import math

def maxMin(k, arr):

    arr.sort()

    out = math.inf

    for i in range(len(arr)-k+1):

        big = arr[i+k-1]
        small = arr[i]

        out = min(out, big-small)

    return out