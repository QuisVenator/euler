digit_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand"
}

def number_to_words(n):
    if n in digit_word:
        return digit_word[n]
    elif n < 100:
        tens = n // 10 * 10
        ones = n % 10
        return digit_word[tens] + digit_word[ones]
    else:
        hundreds = n // 100
        tens = n % 100
        if tens == 0:
            return digit_word[hundreds] + "hundred"
        else:
            return digit_word[hundreds] + "hundredand" + number_to_words(tens)

result = ""
for i in range(1, 1001):
    result += number_to_words(i)
print(len(result))