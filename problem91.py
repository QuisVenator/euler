points = []

for x in range (0, 51):
    for  y in range(0, 51):
        points.append([x,y])

def is_right_angle(p1, p2, p3):
    a = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    b = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
    c = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
    sides = [a,b,c]
    sides.sort()
    return sides[0] + sides[1] == sides[2]

count = 0
for i in range(1, len(points)):
    for j in range(i+1, len(points)):
            if is_right_angle(points[0], points[i], points[j]):
                count += 1

print(count)
