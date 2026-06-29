n1 = list(input())
n2 = list(input())
B = True
for i in set(n1):
    if n1.count(i) != n2.count(i):
        B = False
        break
if len(n1) != len(n2):
    B = False
if B:
    print("Is anagram")
else:
    print("not anagram")
