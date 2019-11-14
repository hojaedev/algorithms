# def solution(user_id, banned_id):
#     answer = 0
#     for bid in banned_id:
#         count = 0
#         for uid in user_id:
#
#             if len(bid) == len(uid):
#
#                 d = dict(zip(a,b))
#
#                 print(d)
#
#                 count += 1 if all(k==v or v == '*' for k,v in d.items()) else 0
#
#         if count != 0:
#             if answer == 0:
#                 answer += count
#             else:
#                 answer *= count
#
#     return answer
#
#
# a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# b = ["fr*d*", "abc1**"]
#
# print(solution(a,b))
from pprint import pprint
import re, queue
from collections import deque,defaultdict,Counter
from itertools import combinations
import math
def solution(user_id, banned_id):

    banned_dict = defaultdict(set)
    banned_dict_dup = Counter(banned_id)

    for i in range(len(banned_id)):

        for j in range(len(user_id)):

            if len(banned_id[i]) == len(user_id[j]):

                z = zip(banned_id[i], user_id[j])

                if all(v[0] == v[1] or v[0] == '*' for i, v in enumerate(z)):
                    banned_dict[banned_id[i]].add(user_id[j])

    answer = 1
    a = []
    for k, v in banned_dict.items():

        answer *= math.factorial(len(v)) // math.factorial(banned_dict_dup[k]) // math.factorial(len(v) - banned_dict_dup[k])
        a.append(v)
    for uid in user_id:

        sub = 1
        count = 0

        for k,v in banned_dict.items():

            if uid in v:

                count += 1
                continue

            sub *= len(v) // banned_dict_dup[k]

        if count > 1:
            answer -= sub

    return answer


print(solution(["frodo", "fradi", "krodo", "crodo", "abc123", "frodoc"]	, ["*rodo", "*rodo", "******"]	))

