with open("inputs/0089_roman.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

def roman_to_int(roman):
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    value = 0
    last = "M"
    temp = 0
    for c in roman:
        if roman_values[c] > roman_values[last]:
            value -= temp
            temp = 0
        elif roman_values[c] < roman_values[last]:
            value += temp
            temp = 0
        temp += roman_values[c]
        last = c
    
    value += temp
    return value

def int_to_roman(n):
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_values = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    roman = ""
    for value in reversed(values):
        while n >= value:
            n -= value
            roman += roman_values[value]
    
    return roman

saved = 0
for line in lines:
    saved += len(line) - len(int_to_roman(roman_to_int(line)))

print(saved)