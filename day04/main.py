import re
from collections import defaultdict

def calculator(points):
    calc = 2
    for i in range(1, points - 1):
        calc *= 2
    return calc

with open('puzzle_input.txt', 'r') as input:
    total = 0
    for row in input:
        data = row.strip().split(":")
        ticket = data[1].split("|")
        winning_numbers = set(re.findall(r'\d+', ticket[0]))
        my_numbers = set(re.findall(r'\d+', ticket[1]))
        winner_numbers = list(winning_numbers & my_numbers)
        points = len(winner_numbers)
        if points > 2:
            points = calculator(points)
        total += points
    print(f"The sum is: {total}")

# Part 2

instances = defaultdict(int)

with open('puzzle_input.txt', 'r') as input:
    for index, row in enumerate(input):
        data = row.strip().split(":")
        ticket = data[1].split("|")
        winning_numbers = set(re.findall(r'\d+', ticket[0]))
        my_numbers = set(re.findall(r'\d+', ticket[1]))
        winner_numbers = list(winning_numbers & my_numbers)
        points = len(winner_numbers)
        instances[index] += 1
        if points > 0:
            for i in range(0, instances[index]):
                for j in range(0, points):
                    instances[index+j+1] += 1
    total = sum(instances.values())
    print(f"The sum is: {total}")