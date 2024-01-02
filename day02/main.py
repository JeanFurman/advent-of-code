import re

# Part 1

colors = {
    'blue': 14,
    'green': 13,
    'red': 12,
}

with open('puzzle_input.txt', 'r') as input:
    total = 0
    verify = 0
    possible = True
    for row in input:
        data = row.strip().split(":")
        colors_data = data[1].split(";")
        for color_data in colors_data:
            color = color_data.split(",")
            for c in color:
                value = re.findall(r'(\d+|[a-zA-Z]+)', c)
                if int(value[0]) <= colors.get(value[1]):
                    verify += 1
            if verify != len(color):
                possible = False
                break
            verify = 0
        if possible:
            total += int(re.findall(r"\d+", data[0])[0])
        possible = True
        verify = 0
    print(f"The sum is: {total}")

# Part 2

colors = {
    'blue': 0,
    'green': 0,
    'red': 0,
}

with open('puzzle_input.txt', 'r') as input:
    total = 0
    for row in input:
        data = row.strip().split(":")
        colors_data = data[1].replace(';', ',').split(',')
        for color_data in colors_data:
            value = re.findall(r'(\d+|[a-zA-Z]+)', color_data)
            if int(value[0]) > colors.get(value[1]):
                colors[value[1]] = int(value[0])
        total += colors['blue'] * colors['green'] * colors['red']
        colors['blue'] = 0
        colors['green'] = 0
        colors['red'] = 0
    print(f"The sum is: {total}") 