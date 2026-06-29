n = list(map(int, input().split()))
t = int(input())
seen = {}
for i in range(len(n)):
    comp = t - n[i]
    if comp in seen:
        print([seen[comp], i])
        break
    seen[n[i]] = i
