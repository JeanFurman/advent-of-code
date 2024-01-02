import numpy as np
import re

def casting_values(content):
    return [int(value) for value in re.findall(r'[-+]?\d+', content)]

i = 1
total = 0
with open('puzzle_input.txt', 'r') as file:
    for row in file:
        sequences = []
        history = casting_values(row.strip())
        sequences.append(history)
        while True:
            sequences.append(list(np.diff(history)))
            if all(seq == 0 for seq in sequences[i]):
                break
            history = sequences[i]
            i += 1
        i = 1
        sequences.reverse()
        v1 = 0
        for seq in sequences:
            seq.append(v1 + seq[-1])
            v1 = seq[-1]
        total += sequences[-1][-1]
    print(total)

# Part 2

i = 1
total = 0
with open('puzzle_input.txt', 'r') as file:
    for row in file:
        sequences = []
        history = casting_values(row.strip())
        sequences.append(history)
        while True:
            sequences.append(list(np.diff(history)))
            if all(seq == 0 for seq in sequences[i]):
                break
            history = sequences[i]
            i += 1
        i = 1
        sequences.reverse()
        v1 = 0
        for seq in sequences:
            v2 = seq[0] - v1
            seq.insert(0, v2)
            v1 = seq[0]
        total += sequences[-1][0]
        print(sequences)
    print(total)

    