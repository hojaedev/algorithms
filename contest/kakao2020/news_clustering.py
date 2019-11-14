import collections, string, re

def solution(str1, str2):

    # REGEX --> clear duplicates --> whitespace replace with non-ascii
    str1 = ''.join(re.findall("[a-z]+", str1.lower()))
    str2 = ''.join(re.findall("[a-z]+", str2.lower()))

    str1 = str1.lower()
    str2 = str2.lower()


    st1 = [''.join(pair) for pair in zip(str1[:-1], str1[1:])]
    st2 = [''.join(pair) for pair in zip(str2[:-1], str2[1:])]

    st1 = filter(lambda x: x[0] in string.ascii_lowercase and x[1] in string.ascii_lowercase, st1)
    st2 = filter(lambda x: x[0] in string.ascii_lowercase and x[1] in string.ascii_lowercase, st2)

    st1 = collections.Counter(list(st1))
    st2 = collections.Counter(list(st2))

    union = st1 | st2
    intersection = st1 & st2

    union_sum = sum(union.values())
    intersection_sum = sum(intersection.values())
    if union_sum == 0:
        return 65536
    return int(intersection_sum / union_sum * 65536)


print(solution('FRANCE', 'FRENCH'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
