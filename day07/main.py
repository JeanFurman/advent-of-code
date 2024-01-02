from collections import Counter
from itertools import count

with open('puzzle_input.txt', 'r') as file:
    content = file.readlines()

strength_ruler = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# five_of_a_kind - 0
# four_of_a_kind - 1
# full_house - 2
# three_of_a_kind - 3
# two_pair - 4
# one_pair - 5
# high_card - 6
types = [{}, {}, {}, {}, {}, {}, {}]

def order_by_strength(cards):
    return dict(sorted(cards.items(), key=lambda item: [strength_ruler.index(c) for c in item[0]]))

for row in content:
    card = row.strip().split(" ")
    char_amount = Counter(card[0].lower())
    amount = char_amount.values()
    if 5 in amount:
        types[0][card[0]] = card[1]
        continue
    if 4 in amount:
        types[1][card[0]] = card[1]
        continue
    if 3 in amount:    
        if 2 in amount:
            types[2][card[0]] = card[1]
            continue
        types[3][card[0]] = card[1]
        continue
    if 2 in amount:   
        if len(amount) == 3:
            types[4][card[0]] = card[1]
            continue
        types[5][card[0]] = card[1]
        continue
    types[6][card[0]] = card[1]
    continue

for i in range(0, 7):
    types[i] = order_by_strength(types[i])

total = 0
multiplier = count(1)
types.reverse()
for t in types:
    for v in t.values():
        total += int(v) * next(multiplier)

print(f'The total winnings is: {total}')

# Part 2

strength_ruler = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
types = [{}, {}, {}, {}, {}, {}, {}]

def order_by_strength(cards):
    return dict(sorted(cards.items(), key=lambda item: [strength_ruler.index(c) for c in item[0]]))

for row in content:
    card = row.strip().split(" ")
    char_amount = Counter(card[0].lower())
    keys = char_amount.keys()
    jocker_value = char_amount.get("j", None)
    if jocker_value is not None and jocker_value < 5:
        del char_amount["j"]
        max_amount = max(char_amount, key=lambda chave: char_amount[chave])
        char_amount[max_amount] = char_amount[max_amount] + jocker_value
    amount = char_amount.values()
    if 5 in amount:
        types[0][card[0]] = card[1]
        continue
    if 4 in amount:
        types[1][card[0]] = card[1]
        continue
    if 3 in amount:    
        if 2 in amount:
            types[2][card[0]] = card[1]
            continue
        types[3][card[0]] = card[1]
        continue
    if 2 in amount:   
        if len(amount) == 3:
            types[4][card[0]] = card[1]
            continue
        types[5][card[0]] = card[1]
        continue
    types[6][card[0]] = card[1]
    continue

for i in range(0, 7):
    types[i] = order_by_strength(types[i])

total = 0
multiplier = count(1)
types.reverse()
for t in types:
    for v in t.values():
        total += int(v) * next(multiplier)

print(f'The total winnings is: {total}')