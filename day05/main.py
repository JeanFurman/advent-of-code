import re

with open('puzzle_input.txt', 'r') as file:
    first_seed = file.readline()
    file.readline()
    content = [row.strip() for row in file.readlines()]

def casting_values(content):
    return [int(seed) for seed in re.findall(r'\d+', content)]

total = 0
dataI = casting_values(first_seed)
dataO = []
removeItens = []
i = 0
while i < len(content):
    if content[i] and content[i][0].isalpha():
        i += 1
        while content[i] and content[i][0].isdigit():
            values = casting_values(content[i])
            initialInputValue = values[1]
            finalInputValue = values[1] + (values[2] - 1)
            initialOutputValue = values[0]
            for v in dataI:
                if v >= initialInputValue and v <= finalInputValue:
                    dataO.append(initialOutputValue + (v - initialInputValue))
                    removeItens.append(v)
            for r in removeItens:
                dataI.remove(r)
            i += 1
            removeItens = []
            if i == len(content):
                break
        if len(dataI) > 0:
            dataO += dataI
        dataI = dataO
        dataO = []
    i += 1

print(f"The lowest location is: {min(dataI)}")

# Part 2

def make_seeds(seeds):
    total = []
    for i in range(0, len(seeds), 2):
        total.append(seeds[i])
        total.append(seeds[i] + seeds[i+1] - 1)
    return total

total = 0
seeds = casting_values(first_seed)
dataI = make_seeds(seeds)
dataO = []
removeItens = []
dataIEx = []
i = 0
while i < len(content):
    if content[i] and content[i][0].isalpha():
        i += 1
        while content[i] and content[i][0].isdigit():
            values = casting_values(content[i])
            initialInputValue = values[1]
            finalInputValue = values[1] + (values[2] - 1)
            initialOutputValue = values[0]
            finalOutputValue = values[0] + (values[2] - 1)
            for v in range(0, len(dataI), 2):
                initialSeedValue = dataI[v]
                finalSeedValue = dataI[v+1]
                if finalSeedValue > initialInputValue and initialSeedValue < finalInputValue:
                    if finalSeedValue > finalInputValue and finalSeedValue > initialSeedValue:
                        dataIEx.append(finalInputValue + 1)
                        dataIEx.append(finalSeedValue)
                        finalSeedValue = finalInputValue
                    if initialSeedValue < initialInputValue:
                        dataIEx.append(initialSeedValue)
                        dataIEx.append(initialInputValue - 1)
                        initialSeedValue = initialInputValue 
                    dataI[v] = initialSeedValue
                    dataI[v+1] = finalSeedValue
                    dataO.append(initialOutputValue + (initialSeedValue - initialInputValue))
                    dataO.append(initialOutputValue + (finalSeedValue - initialInputValue))
                    removeItens.append(initialSeedValue)
                    removeItens.append(finalSeedValue)
            for r in removeItens:
                dataI.remove(r)
            i += 1
            removeItens = []
            dataI += dataIEx
            dataIEx = []
            if i == len(content):
                break
        if len(dataI) > 0:
            dataO += dataI
        dataI = dataO
        dataO = []
    i += 1
print(f"The lowest location is: {min(dataI)}")