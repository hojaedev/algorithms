import collections


def solution(cacheSize, cities):
    time = 0

    d = collections.OrderedDict()

    for i in range(len(cities)):

        city = cities[i].lower()

        if city in d.keys():

            time += 1

            d.move_to_end(city, True)

        else:

            time += 5

            d[city] = 0

            if len(d) > cacheSize:
                d.popitem(False)

    return time


cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(2, cities))
