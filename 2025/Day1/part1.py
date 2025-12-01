input = []
with open('test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())

print(input)