matrix = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

i = 0
j = 0

line = []

for i in matrix:
    for j in i:
        line.append(matrix[j[0]][j[1]])

print(line)


