input = []
position = 50
solution = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())

for i in input:
    direction = i[0]
    value = int(i[1:])
    if direction == 'L':
        value *= -1
    sum = position + value
    if (sum > 99):
        solution += sum // 100
    elif (sum <= 0 and position != 0):
        solution += (abs(sum) // 100) + 1
    elif (sum <= 0):
        solution += (abs(sum) // 100)
    position = sum % 100
  
print(solution)