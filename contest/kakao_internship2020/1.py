from collections import *
import itertools
import operator
def solution(s):

    a = s[2:len(s)-2].split('},{')
    a = list(map(lambda x: list(map(int, x.split(','))), a))
    a.sort(key= lambda x: len(x))

    if len(a) == 1:
        return list(map(int, a[0]))

    answer = [a[0][0]]
    for i in range(1,len(a)):
        diff = set(a[i]) - set(a[i-1])

        answer.append(diff.pop())

    return answer

# print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))
# print(solution('{{123}}'))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{2,1,3,4},{2,1},{2,1,3},{2}}"))



