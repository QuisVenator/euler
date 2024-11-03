
card_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def is_straight(hand):
    for i in range(1, len(hand)):
        if hand[i] - hand[i-1] != 1:
            return False
    return True

def is_flush(suits):
    return len(set(suits)) == 1

def is_straight_flush(hand, suits):
    return is_straight(hand) and is_flush(suits)

def is_royal_flush(hand, suits):
    return is_straight_flush(hand, suits) and hand[0] == 10

def is_four_of_a_kind(hand):
    return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4

def is_pair(hand):
    return hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2 or hand.count(hand[2]) == 2 or hand.count(hand[3]) == 2

def is_three_of_a_kind(hand):
    return hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3

def is_full_house(hand):
    return is_pair(hand) and is_three_of_a_kind(hand)

def is_two_pairs(hand):
    card_dict = {}
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    return len(card_dict) == 3 and 2 in card_dict.values()

def score_four_of_a_kind(hand):
    if hand.count(hand[0]) == 4:
        return [8, hand[0], hand[4]]
    else:
        return [8, hand[1], hand[0]]
    
def score_full_house(hand):
    triple = None
    pair = None
    for card in hand:
        if hand.count(card) == 3:
            triple = card
        elif hand.count(card) == 2:
            pair = card
    return [7, triple, pair]

def score_two_pairs(hand):
    pair1 = None
    pair2 = None
    kicker = None
    for card in hand:
        if hand.count(card) == 2:
            if pair1 is None:
                pair1 = card
            elif card != pair1:
                pair2 = card
        else:
            kicker = card
    if pair2 > pair1:
        pair1, pair2 = pair2, pair1
    return [3, pair1, pair2, kicker]

def score_pair(hand):
    pair = None
    kickers = []
    for card in hand:
        if hand.count(card) == 2:
            pair = card
        else:
            kickers.append(card)
    result = [2, pair]
    result.extend(reversed(kickers))
    return result

def score_three_of_a_kind(hand):
    triple = None
    kickers = []
    for card in hand:
        if hand.count(card) == 3:
            triple = card
        else:
            kickers.append(card)
    result = [4, triple]
    result.extend(reversed(kickers))
    return result

def score_hand(hand, suits):
    if is_royal_flush(hand, suits):
        return [10]
    elif is_straight_flush(hand, suits):
        return [9, hand[-1]]
    elif is_four_of_a_kind(hand):
        return score_four_of_a_kind(hand)
    elif is_full_house(hand):
        return score_full_house(hand)
    elif is_flush(suits):
        return [6, hand[-1]]
    elif is_straight(hand):
        return [5, hand[-1]]
    elif is_three_of_a_kind(hand):
        return score_three_of_a_kind(hand)
    elif is_two_pairs(hand):
        return score_two_pairs(hand)
    elif is_pair(hand):
        return score_pair(hand)
    else:
        return [1, hand[-1], hand[-2], hand[-3], hand[-4], hand[-5]]

def compare_hands(hand1, suits1, hand2, suits2):
    score1 = score_hand(hand1, suits1)
    score2 = score_hand(hand2, suits2)
    
    for i in range(len(score1)):
        if score1[i] > score2[i]:
            return 1
        elif score1[i] < score2[i]:
            return 2
        
    return 0


with open("inputs/0054_poker.txt") as f:
    games = f.readlines()

count = 0
for game in games:
    cards = game.split()
    hand1 = []
    hand2 = []
    suits1 = []
    suits2 = []
    for card in cards[:5]:
        hand1.append(card_dict[card[0]])
        suits1.append(card[1])
    for card in cards[5:]:
        hand2.append(card_dict[card[0]])
        suits2.append(card[1])
    hand1.sort()
    hand2.sort()
    
    if compare_hands(hand1, suits1, hand2, suits2) == 1:
        count += 1

print(count)
        
