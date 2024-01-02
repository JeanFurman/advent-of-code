import re
from collections import OrderedDict
import math

content = OrderedDict()

with open('puzzle_input.txt', 'r') as file:
    instructions  = file.readline().strip()
    file.readline()
    for row in file:
        key, value = row.strip().split("=")
        value = re.findall(r'\b\w+\b', value)
        content[key.replace(" ", "")] = value

# steps = 0
# way = "AAA"
# directions = {"L": 0, "R": 1}
# i = 0
# while True:
#     choices = content[way]
#     choice = choices[directions.get(instructions[i])]
#     steps += 1
#     i += 1
#     if choice == "ZZZ":
#         break
#     if i == len(instructions):
#         i = 0
#     way = choice

# print(f'The total steps is: {steps}')

# Part 2

steps = 0
initial_ways = [key for key in content.keys() if key.endswith('A')]
directions = {"L": 0, "R": 1}
i = 0
total = 0
Z_ways = {}
while True:
    ways = []
    steps += 1
    for way in initial_ways:
        choices = content[way]
        choice = choices[directions.get(instructions[i])]
        if choice.endswith('Z'):
            Z_ways[choice] = steps
        ways.append(choice)
    i += 1
    if i == len(instructions):
        i = 0
    initial_ways = ways
    if len(Z_ways) == len(initial_ways):
        total = math.lcm(*Z_ways.values())
        break

print(f'The total steps is: {total}')