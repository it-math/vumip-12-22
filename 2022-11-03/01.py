x = int(input())

if x > 10:
    y = x + 10
elif x > 5:
    y = 2 * x + 3
elif x > 2:
    y = x - 5
elif x > -1:
    y = x + 1
else:
    y = x
print(y)
