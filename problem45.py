i_triangle = 285
i_pentagonal = 165
i_hexagonal = 143

triangle = None
pentagonal = None
hexagonal = None

def get_next_triangle():
    global i_triangle, triangle
    i_triangle += 1
    triangle = i_triangle * (i_triangle + 1) // 2

def get_next_pentagonal():
    global i_pentagonal, pentagonal
    i_pentagonal += 1
    pentagonal = i_pentagonal * (3 * i_pentagonal - 1) // 2

def get_next_hexagonal():
    global i_hexagonal, hexagonal
    i_hexagonal += 1
    hexagonal = i_hexagonal * (2 * i_hexagonal - 1)

get_next_triangle()
get_next_pentagonal()
get_next_hexagonal()

while triangle != pentagonal or triangle != hexagonal:
    if triangle < pentagonal:
        if triangle < hexagonal:
            get_next_triangle()
        else:
            get_next_hexagonal()
    else:
        if pentagonal < hexagonal:
            get_next_pentagonal()
        else:
            get_next_hexagonal()

print(f"Found: {triangle} = {pentagonal} = {hexagonal} for indices {i_triangle}, {i_pentagonal}, {i_hexagonal}")

