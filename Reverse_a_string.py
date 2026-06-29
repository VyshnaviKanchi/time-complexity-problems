n = list(input())
for i in range(len(n)//2):
    j = -1 - i
    n[i], n[j] = n[j], n[i]
print("".join(n))
