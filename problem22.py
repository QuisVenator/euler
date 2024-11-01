
with open("inputs/0022_names.txt") as f:
    names = f.read().split(",")
    names = [name.strip("\"") for name in names]
    names.sort()

alphabet = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

score = 0
for i, name in enumerate(names):
    score += sum([alphabet[letter] for letter in name]) * (i + 1)

print(score)
