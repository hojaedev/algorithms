'''
HackerRank
Hashmap
Count Triplets
'''
from collections import Counter
def countTriplets(arr, r):

    next = Counter(arr)

    prev = {}

    if len(arr) == 0:

        return 0

    prev[arr[0]] = 1
    next[arr[0]] -= 1

    count = 0

    for i in range(1, len(arr)-1):

        next[arr[i]] -= 1

        if arr[i] % r == 0 and arr[i]//r in prev and arr[i] * r in next:

            count += prev[arr[i]//r] * (next[arr[i]*r])

        if arr[i] in prev:

            prev[arr[i]] += 1

        else:

            prev[arr[i]] = 1

    return count

a, b = map(int, input().split())

print(countTriplets(list(map(int, input().split(" "))),b))

'''
HackerRank
Hashmap
Frequency Queries
'''

import sys
def freqQuery(queries):

    out = ''

    count = {0: 0}

    d = {}

    for i in range(len(queries)):

        n = queries[i][0]
        k = queries[i][1]


        f = d.get(k, 0)

        # reduce 1 or increase 1 to the changed item
        if n == 1:
            d[k] = f + 1
            count[f+1] = count.get(f+1,0) + 1
            count[f] = max(count.get(f,0)-1, 0)
        elif n == 2:
            d[k] = max(f - 1, 0)
            count[f-1] = count.get(f-1,0) + 1
            count[f] = max(count.get(f,0)-1,0)
        else:
            out += '1' if count.get(k, 0) else '0'

    return out

'''
HackerRank
Hashmap
Ransom Note
'''
from collections import Counter
def checkMagazine(magazine, note):
    a = magazine
    b = note

    c1 = Counter(a)
    c2 = Counter(b)

    c1.subtract(c2)
    print(c1)
    for k, v in c1.items():
        if v < 0:
            return 'No'
    return 'Yes'

mn = input().split()

m = int(mn[0])

n = int(mn[1])

magazine = input().rstrip().split()

note = input().rstrip().split()

print(checkMagazine(magazine, note))



'''
Programmers
Hashmap
'''

from collections import defaultdict
from itertools import combinations
from functools import reduce

def solution(clothes):
    d = defaultdict(list)
    for k, v in clothes:
        d[k].append(v)

    a = []

    for k, v in d.items():

        a.append(len(v))

    for i in range(1,6):
        combinations(a, i)

    return 0
