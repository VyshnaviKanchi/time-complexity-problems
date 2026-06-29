n1 = list(input())
n2 = list(input())
char = {}
B = True
for ch in n1:
    if ch not in char:
        char[ch] = 0
    char[ch] += 1
for ch in n2:
    if ch not in char or char[ch]  == 0:
        B = False
        break
    char[ch] -= 1

for ch in char.values():
    if ch != 0:
        B = False
if len(n1) != len(n2):
    B = False
if B:
    print("Is anagram")
else:
    print("not anagram")
