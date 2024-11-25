from itertools import permutations

digit_perms = list(permutations("123456789"))
print(len(digit_perms))

def largest_square_anagrams(word1, word2):
    res = 0
    letters = set(word1)
    ori_word1 = word1
    ori_word2 = word2

    for perm in digit_perms:
        word1 = ori_word1
        word2 = ori_word2
        for i, letter in enumerate(letters):
            word1 = word1.replace(letter, perm[i])
        
        if word1[0] == "0":
            continue
        num1 = int(word1)
        if int(num1**0.5)**2 == num1:
            for i, letter in enumerate(letters):
                word2 = word2.replace(letter, perm[i])
            
            if word2[0] == "0":
                continue
            num2 = int(word2)
            if int(num2**0.5)**2 == num2:
                res = max(res, num1, num2)
    
    return res

words = []
with open("inputs/0098_words.txt") as f:
    words = f.read().split(",")
    words = [word[1:-1] for word in words]

anagrams = {}
for word in words:
    key = "".join(sorted(word))
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]

max_square = 0
for key in anagrams:
    if len(anagrams[key]) > 1:
        pairs = anagrams[key]

        for i in range(len(pairs)):
            for j in range(i+1, len(pairs)):
                max_square = max(max_square, largest_square_anagrams(pairs[i], pairs[j]))

print(max_square)
