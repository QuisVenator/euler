

word_values = {}
with open('inputs/0042_words.txt') as f:
    words = f.read().replace('"','').split(',')

print(words[:5])

start_val = ord('A') - 1
max_word_val = 0
for word in words:
    value = sum(ord(c) - start_val for c in word)
    word_values[value] = word_values.get(value, 0) + 1
    max_word_val = max(max_word_val, value)

triangular_numbers = set()
i = 0
num = 0
while num < max_word_val:
    i += 1
    num = i * (i + 1) // 2
    triangular_numbers.add(num)
    

count = 0
for word, wc in word_values.items():
    if word in triangular_numbers:
        count += wc

print(f"Threre are {count} triangular words")

