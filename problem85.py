def count_rectangles_contained(n, m):
    count = 0
    for a in range(1, n+1):
        for b in range(1, m+1):
            count += (n - a + 1) * (m - b + 1)
    
    return count

nearest = float("inf")
nearest_area = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        count = count_rectangles_contained(i, j)
        
        if abs(count - 2_000_000) < nearest:
            nearest = abs(count - 2_000_000)
            nearest_area = i * j

        if count > 2_000_000:
            break
    
    if i % 10 == 0:
        print(f"Progress: {i}, {i / 1000 *100:.2f}%", end="\r")

print()

print(nearest_area)