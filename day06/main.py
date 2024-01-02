import re
from operator import mul
from functools import reduce

def casting_values(content):
    return [int(value) for value in re.findall(r'\d+', content)]

with open('puzzle_input.txt', 'r') as file:
    content = file.readlines()

times = casting_values(content[0])
distances = casting_values(content[1])
records = []

for index, t in enumerate(times):
    record_counter = 0
    for i in range(1, t):
        if i * (t-i) > distances[index]:
            record_counter += 1
    records.append(record_counter)

print(f'The multiplication of the number of records is: {reduce(mul, records, 1)}')

# Part 2

times = int(''.join(re.findall(r'\b\d+\b', content[0])))
distances = int(''.join(re.findall(r'\b\d+\b', content[1])))

record_counter = 0
for i in range(1, times):
    if i * (times-i) > distances:
        record_counter += 1

print(f'The number of ways to beat the record is: {record_counter}')


