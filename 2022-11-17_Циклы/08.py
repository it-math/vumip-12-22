x = int(input())
s = 0
i = 1
while i <= 10:
    j = 2
    while j <= 5:
        s += x ** j / (i + 2)
        j += 1
    i += 1
print(s)
