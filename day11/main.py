from itertools import count

with open('puzzle_input.txt', 'r') as file:
    content = [list(line.strip()) for line in file]

def amount_of_dots(index, qnt):
    if index == 0:
        return 0
    return qnt * index 

def add_dot_rows(content):
    dots = []
    for i, x in enumerate(content):
        if not "#" in x:
            dots.append(i)
    return dots

def finding_sharp(row, sharp):
    position = -1
    while True:
        position = row.find(sharp, position + 1)
        if position == -1:
            break
        yield position

def calculate_row_column(data, s):
    pos = 0
    if max(data) < s:
        return s + amount_of_dots(len(data), amount_rows_and_cols)
    for index, d in enumerate(data):
        if s < d:
            pos = s + amount_of_dots(index, amount_rows_and_cols)
            break
    return pos

cols = []
for col in range(len(content[0])):
    if all(x == "." for x in [row[col] for row in content]):
        cols.append(col)

amount_rows_and_cols = 999_999
rows = add_dot_rows(content)
galaxies = count(1)
galaxies_position = {}
max_galaxies = 0

for i, x in enumerate(content):
    if "#" in x:
        sharp = list(finding_sharp(''.join(x), '#'))
        for s in sharp:
            max_galaxies = next(galaxies)
            x[s] = max_galaxies
            posS = calculate_row_column(cols, s)
            posI = calculate_row_column(rows, i)
            galaxies_position[str(max_galaxies)] = (posI, posS) 

galaxies_pairs = set()
control = 1
while control < max_galaxies:
    for x in range(control + 1, max_galaxies + 1):
        galaxies_pairs.add((control, x))
    control += 1

total = 0

for (g1, g2) in galaxies_pairs:
    (row1, col1) = galaxies_position.get(str(g1))
    (row2, col2) = galaxies_position.get(str(g2))
    
    if row1 > row2:
        total+= row1 - row2
    else:
        total+= row2 - row1
    if col1 > col2:
        total+= col1 - col2
    else:
        total+= col2 - col1

print(total)
