cards = [i+1 for i in range(int(input()))]
p = 0
while p < len(cards)-1:
    if p % 2 == 1:
        cards.append(cards[p])
    p += 1

print(cards[-1])