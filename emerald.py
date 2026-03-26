a = int(input())
b = [2,3,4,6,7,2,8,2,4,3]
current = 0
best = 0
for i in range(len(b)):
    if b[i] % 2 == 0:
        current += b[i]
    else:
        current = 0
    if current > best:
        best = current
print(best)
