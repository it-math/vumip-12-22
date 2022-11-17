x = int(input())
s = 0
for i in range(1, 10+1):
    for j in range(2, 6):
        s += x ** j / (i + 2)
print(s)
