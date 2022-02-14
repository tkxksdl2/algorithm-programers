def solution(cacheSize, cities):
    answer = 0
    cathe = []
    cities = [city.lower() for city in cities]

    if cacheSize==0: return len(cities) * 5 

    for city in cities:
        if city in cathe:
            answer += 1
            cathe.append(cathe.pop(cathe.index(city)))
        else:
            answer += 5
            if len(cathe) < cacheSize:
                cathe.append(city)
            else:
                cathe.pop(0)
                cathe.append(city)
        print(cathe)
        print(answer)
    return answer

cacheSize = 2
cities =["Jeju", "Pangyo", "NewYork", "newyork"]

print(solution(cacheSize, cities))