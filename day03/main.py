from collections import deque

simbols = ["@", "*", "/", "#", "%", "$", "&", "-", "=", "+"]

with open('puzzle_input.txt', 'r') as file:
    content = [list(line.strip()) for line in file]

def test_grid_position(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return grid[i][j]
    else:
        return ""
    
total = 0
for i in range(0, len(content)):
    j=0
    number = ""
    digit = False
    position = deque()
    while j < len(content[i]):
        c = 0
        auxI = i - 1
        while test_grid_position(content, i, j).isdigit():
            number += test_grid_position(content, i, j)
            position.append(j)
            j += 1
            digit = True
        if digit:
            position.appendleft(position[0] - 1)
            position.append(position[-1] + 1)
            for x in range(0, 3):
                for c in position:
                    if test_grid_position(content, auxI, c) in simbols:
                        total += int(number)
                        break
                auxI += 1
        j += 1
        digit = False
        number = ""
        position.clear()

print(f"The sum is: {total}") 

# Part 2
    
total = 0
for i in range(0, len(content)):
    j=0
    number = ""
    while j < len(content[i]):
        mult = []
        auxI = i - 1
        if test_grid_position(content, i, j) == "*":
            for x in range(0, 3):
                counter = j - 1
                while counter <= j + 1:
                    control = 1
                    if test_grid_position(content, auxI, counter).isdigit():
                        x = 1
                        while test_grid_position(content, auxI, counter - x).isdigit():
                            number += test_grid_position(content, auxI, counter - x)
                            x += 1
                        number = number[::-1]
                        number += test_grid_position(content, auxI, counter)
                        while test_grid_position(content, auxI, counter + control).isdigit():
                            number += test_grid_position(content, auxI, counter + control)
                            control += 1
                        mult.append(int(number))
                    number = ""
                    counter += control
                auxI += 1
                if len(mult) > 1:
                    total += mult[0] * mult[1]
                    break
            mult = []
        j += 1
        number = ""

print(f"The sum is: {total}") 
