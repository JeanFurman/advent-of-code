from itertools import product
import re

with open('puzzle_input.txt', 'r') as file:
    content = [row.strip() for row in file.readlines()]

def validate_contiguous(combination, numbers):
    sharps = re.findall(r'#+', combination)
    numbers_sharps = [str(len(sharp)) for sharp in sharps]
    return numbers == numbers_sharps

def possible_combinations(spring):
    possibilities = ['.' , '#'] 
    unknowns = [i for i, char in enumerate(spring) if char == '?']
    combinations = []

    for combination in product(possibilities, repeat=len(unknowns)):
        new_combination = list(spring)
        for i, u in zip(unknowns, combination):
            new_combination[i] = u
        combinations.append(''.join(new_combination))

    return combinations

arrangements = 0
multiplier = 1 # multiplier for part 2
for row in content:
    springs, contiguous_group = row.split(" ")
    spring = springs
    springs += "?"
    springs = springs * multiplier 
    springs = springs[:-1]
    unknowns = list(possible_combinations(springs))
    print(len(unknowns))
    for u in unknowns:
        if validate_contiguous(u, contiguous_group.split(",") * multiplier):
            arrangements += 1

print(f'The sum of the arrangements is {arrangements}')
