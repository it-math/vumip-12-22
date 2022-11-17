n = int(input('n = '))
s = 0
k = 0
for i in range(n):
    x = int(input('x = '))
    if x > 0:
        s += x
        k += 1
    elif x < 0:
        continue
    s += 5
else:
    print('ok')

print(s)
print(k)
print(s / k)