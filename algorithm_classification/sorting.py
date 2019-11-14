
'''
HackerRank
Sorting
Comparator
'''

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):

        if a.score < b.score:

            return 1

        elif a.score == b.score:

            if a.name > b.name:

                return 1

            elif a.name == b.name:

                return 0

            else:
                return -1

        else:

            return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


'''
HackerRank
Sorting
Bubble Sort
'''
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[j] < a[i]:
                tmp = a[j]
                a[j] = a[i]
                a[i] = tmp
                count += 1
    print('Array is sorted in {} swaps'.format(count))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]), end='')


countSwaps([1,2,3])
