

with open("inputs/0059_cipher.txt") as f:
    cipher = [int(x) for x in f.read().split(",")]

for a in range(ord('a'), ord('z')+1):
    for b in range(ord('a'), ord('z')+1):
        for c in range(ord('a'), ord('z')+1):
            key = [a, b, c]
            decrypted = []
            for i in range(len(cipher)):
                decrypted.append(cipher[i] ^ key[i % 3])
            decrypted = "".join([chr(x) for x in decrypted])
            if " the " in decrypted:
                print(decrypted)
                print(sum([ord(x) for x in decrypted]))
                break
