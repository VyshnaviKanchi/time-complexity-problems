n = tuple(map(int,input().split()))
maxNum = n[0]
for i in range(1, len(n)):
    if maxNum < n[i]:
        maxNum = n[i]
print(maxNum)
