def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(reverse=True, key=lambda x: x*3)

    answer = ''.join(numbers)

    return answer

numbers = [3, 30, 34, 5, 9, 309, 310, 0]
print(solution(numbers))