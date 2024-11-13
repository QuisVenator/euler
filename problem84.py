from random import randint


field_names = [
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "JAIL",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP",
    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2"
]

ch_index = 0
ch_cards = [
    "GO",
    "JAIL",
    "C1",
    "E3",
    "H2",
    "R1",
    "next_R",
    "next_R",
    "next_U",
    "back_3",
    "CH",
    "CH",
    "CH",
    "CH",
    "CH",
    "CH"
]

cc_index = 0
cc_cards = [
    "GO",
    "JAIL",
]

cc_cards.extend(["CC"] * 14)



def roll_dice():
    return (randint(1, 4), randint(1, 4))

def move(current_position, dice_roll):
    return (current_position + sum(dice_roll)) % 40

def is_chance(position):
    return field_names[position].startswith("CH")

def is_community_chest(position):
    return field_names[position].startswith("CC")

def is_go_to_jail(position):
    return field_names[position] == "G2J"

def next_railroad(position):
    if position < 5:
        return 5
    if position < 15:
        return 15
    if position < 25:
        return 25
    return 35

def next_utility(position):
    if position < 12:
        return 12
    return 28

def next_chance(position):
    global ch_index
    card = ch_cards[ch_index]
    ch_index = (ch_index + 1) % len(ch_cards)
    if card == "GO":
        return 0
    if card == "JAIL":
        return 10
    if card == "C1":
        return 11
    if card == "E3":
        return 24
    if card == "H2":
        return 39
    if card == "R1":
        return 5
    if card == "next_R":
        return next_railroad(position)
    if card == "next_U":
        return next_utility(position)
    if card == "back_3":
        return (position - 3) % 40
    return position

def next_community_chest(position):
    global cc_index
    card = cc_cards[cc_index]
    cc_index = (cc_index + 1) % len(cc_cards)
    if card == "GO":
        return 0
    if card == "JAIL":
        return 10
    return position

def next_position(position):
    if is_go_to_jail(position):
        return 10
    if is_chance(position):
        return next_chance(position)
    if is_community_chest(position):
        return next_community_chest(position)
    return position

def simulate():
    current_position = 0
    counts = [0] * 40
    for i in range(10_000_000):
        dice_roll = roll_dice()
        current_position = move(current_position, dice_roll)
        current_position = next_position(current_position)
        counts[current_position] += 1

        if i % 100_000 == 0:
            print(i, counts)
    return sorted(enumerate(counts), key=lambda x: x[1], reverse=True)

print(simulate())