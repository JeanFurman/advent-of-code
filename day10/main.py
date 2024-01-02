from collections import deque

directions = {"|": 11, "F": 110, "7": 510, "L": 101, "J": 501, "-": 600}

with open('puzzle_input.txt', 'r') as file:
    content = [list(line.strip()) for line in file]

def test_grid_position(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return grid[i][j]
    else:
        return ""
    
pathmap = [['.'] * len(c) for c in content]

def walk(content, start):
    visited = set()
    rows, cols = len(content), len(content[0])
    queue = deque([])
    visited.add((start[0], start[1]))

    n = test_grid_position(content, start[0] - 1, start[1])
    s = test_grid_position(content, start[0] + 1, start[1])
    w = test_grid_position(content, start[0], start[1] - 1)
    e = test_grid_position(content, start[0], start[1] + 1)
    initial = 0
    if n in ["F", "7", "|"]:
        queue.append((start[0] - 1, start[1], 1))
        initial += 1
    if s in ["L", "J", "|"]:
        queue.append((start[0] + 1, start[1], 1))
        initial += 10
    if e in ["J", "7", "-"]:
        queue.append((start[0], start[1] + 1, 1))
        initial += 100
    if w in ["F", "L", "-"]:
        queue.append((start[0], start[1] - 1, 1))
        initial += 500
    pathmap[start[0]][start[1]] = [key for key, v in directions.items() if v == initial][0]
    
    while queue:
        row, col, distance = queue.popleft()
        current = test_grid_position(content, row, col)
        if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and current != ".":
            possible_positions = directions.get(current, None)
            n = test_grid_position(content, row - 1, col)
            s = test_grid_position(content, row + 1, col)
            w = test_grid_position(content, row, col - 1)
            e = test_grid_position(content, row, col + 1)
            if possible_positions == 11:
                if n in ["F", "7", "|"] and (row - 1, col) not in visited:
                    queue.append((row - 1, col, distance + 1))
                elif s in ["L", "J", "|"] and (row + 1, col) not in visited:
                    queue.append((row + 1, col, distance + 1))
            elif possible_positions == 110:
                if e in ["J", "7", "-"] and (row, col + 1) not in visited:
                    queue.append((row, col + 1, distance + 1))
                elif s in ["|", "L", "J"] and (row + 1, col) not in visited:
                    queue.append((row + 1, col, distance + 1))
            elif possible_positions == 510:
                if w in ["F", "L", "-"] and (row, col - 1) not in visited:
                    queue.append((row, col - 1, distance + 1))
                elif s in ["|", "L", "J"] and (row + 1, col) not in visited:
                    queue.append((row + 1, col, distance + 1))
            elif possible_positions == 101:
                if e in ["J", "7", "-"] and (row, col + 1) not in visited:
                    queue.append((row, col + 1, distance + 1))
                elif n in ["F", "7", "|"] and (row - 1, col) not in visited:
                    queue.append((row - 1, col, distance + 1))
            elif possible_positions == 501:
                if w in ["F", "L", "-"] and (row, col - 1) not in visited:
                    queue.append((row, col - 1, distance + 1))
                elif n in ["F", "7", "|"] and (row - 1, col) not in visited:
                    queue.append((row - 1, col, distance + 1))
            elif possible_positions == 600:
                if w in ["F", "L", "-"] and (row, col - 1) not in visited:
                    queue.append((row, col - 1, distance + 1))
                elif e in ["J", "7", "-"] and (row, col + 1) not in visited:
                    queue.append((row, col + 1, distance + 1))
            pathmap[row][col] = current
            visited.add((row, col))
            print(f"The farthest distance is: {distance}")
    return visited

start = [(i, j) for i, row in enumerate(content) for j, value in enumerate(row) if value == "S"]
start_row, start_column = start[0]

visited = walk(content, (start_row, start_column))

newlines = []
for j, line in enumerate(pathmap):
    i = 0
    newline = []
    while i < len(line):
        if line[i] in ["L", "F", "-"]: 
            line.insert(i+1, "-")
        else: line.insert(i+1, ".")
        if line[i] in ["F", "|", "7"]: 
            newline += ["|", "."]
        else: newline += [".", "."]
        i += 2
    newlines.append(newline)
bigmap = [None] * (len(pathmap)*2)
bigmap[::2] = pathmap 
bigmap[1::2] = newlines
bigmap.insert(0, ["."] * len(bigmap[0]))

current_queue = [[0,0]]
while current_queue:
    x, y = current_queue.pop()
    bigmap[y][x] = "O"
    if test_grid_position(bigmap, y, x-1) == ".":
        current_queue.append([x-1, y])
    if test_grid_position(bigmap, y, x+1) == ".":
        current_queue.append([x+1, y])
    if test_grid_position(bigmap, y+1, x) == ".":
        current_queue.append([x, y+1])
    if test_grid_position(bigmap, y-1, x) == ".":
        current_queue.append([x, y-1])

print(sum(line[::2].count(".") for line in pathmap))