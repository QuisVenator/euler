squares = [
    [0,1],
    [0,4],
    [0,9],
    [1,6],
    [2,5],
    [3,6],
    [4,9],
    [8,1]
]

def can_form_squares(cube1, cube2):
    for square in squares:
        if not (square[0] in cube1 and square[1] in cube2) and not (square[0] in cube2 and square[1] in cube1):
            # print(f"Can not form square {square} with cubes {cube1} and {cube2}")
            return False
    return True

cubes = []

for num1 in range(0,10):
    for num2 in range(num1+1,10):
        for num3 in range(num2+1,10):
            for num4 in range(num3+1,10):
                for num5 in range(num4+1,10):
                    for num6 in range(num5+1, 10):
                        cubes.append([num1,num2,num3,num4,num5,num6])
                        if 6 in cubes[-1]:
                            cubes[-1].append(9)
                        if 9 in cubes[-1]:
                            cubes[-1].append(6)

# can_form_squares([0,5,6,7,8,9], [1,2,3,4,8,9])

count = 0
for i in range(len(cubes)):
    for j in range(i, len(cubes)):
        if can_form_squares(cubes[i], cubes[j]):
            count += 1

print(count)
