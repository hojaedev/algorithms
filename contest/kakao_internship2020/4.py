from collections import OrderedDict
def solution(k, room_number):
    arr = [0] * (k+1)
    answer = []
    for q in room_number:

        if not arr[q]:
            answer.append(q)
            arr[q] = 1
        else:
            idx = next((i for i, x in enumerate(arr[q+1:]) if not x), None)
            idx += q + 1
            answer.append(idx)
            arr[idx] = 1
    return answer


print(solution(10, [1,3,4,1,3,1]))

