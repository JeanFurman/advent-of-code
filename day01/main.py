full_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('puzzle_input.txt', 'r') as input:
    total = 0
    numbers = []
    for row in input:
        for index, char in enumerate(row):
            if char.isdigit():
                numbers.append(int(char))
            for i in range(3, 6):
                v = full_numbers.get(row[index:index+i])
                if v is not None:
                    numbers.append(v)
        total += int(f"{numbers[0]}{numbers[-1]}")
        numbers = []
    print(f"The sum is: {total}")