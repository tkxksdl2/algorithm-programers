import re
from collections import Counter

def solution(str1, str2):
    r = re.compile("[a-zA-Z]")
    str1 = Counter([(str1[i] + str1[i+1]).lower() for i in range(len(str1)-1) \
                                    if r.match(str1[i]) and r.match(str1[i+1])])
    str2 = Counter([(str2[i] + str2[i+1]).lower() for i in range(len(str2)-1) \
                                    if r.match(str2[i]) and r.match(str2[i+1])])

    intersection = str1 & str2
    union = str1 | str2
    
    return int((sum(intersection.values()) / sum(union.values())) * 65536) if sum(union.values()) != 0 else 1 * 65536


str1 = 'E=M*C^2'
str2 = 'e=m*c^2'

print(solution(str1, str2))