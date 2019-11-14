def solution(stones, k):
    answer = 1
    a = []
    stones.insert(0,0)
    stones.append(0)
    for i in range(len(stones)-k):

        a.append(max(stones[i:i+k]))

    return min(a)



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([2,5,4,7,8,9,1], 3))

